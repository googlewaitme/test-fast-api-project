from fastapi import APIRouter, Depends, HTTPException
from typing import List

from models.token import Token_Pydantic, TokenIn_Pydantic, Token
from utils.generate_random_string import get_random_string
from loader import contract, w3
import config


router = APIRouter(
    prefix='/tokens',
    responses={404: {"description": "Not found"}},
)


@router.post('/create', response_model=Token_Pydantic)
async def create_token(token: TokenIn_Pydantic):
    unique_hash = get_random_string()

    nonce = w3.eth.get_transaction_count(token.owner)
    lala_txn = contract.functions.mint(
        owner=token.owner,
        uniqueHash=unique_hash,
        mediaURL=token.media_url
    ).buildTransaction({'nonce': nonce})

    signed_txn = w3.eth.account.sign_transaction(
        lala_txn, private_key=config.PRIVATE_KEY
    )
    tx_hash = signed_txn.hash
    w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    token_obj = await Token.create(
        unique_hash=unique_hash,
        tx_hash=tx_hash,
        **token.dict()
    )
    return await Token_Pydantic.from_tortoise_orm(token_obj)


@router.get('/list', response_model=List[Token_Pydantic])
async def get_list_tokens(skip: int = 0, limit: int = 10):
    # TODO pagination
    return await Token_Pydantic.from_queryset(Token.all())


@router.get('/total_supply')
async def get_total_supply():
    """
    Это API должно обращаться к контракту в блокчейне и выдавать в ответе
    информацию о текущем Total supply токена - общем числе находящихся
    токенов в сети.
    Форма ответа - произвольная, в JSON-формате.
    """
    transaction = contract.functions['totalSupply']
    total_supply = transaction().call()
    return {'data': total_supply}
