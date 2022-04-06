from fastapi import APIRouter, Depends, HTTPException
from models.token import Token_Pydantic, TokenIn_Pydantic, Token

from utils.generate_random_string import get_random_string


router = APIRouter(
    prefix='/tokens',
    responses={404: {"description": "Not found"}},
)


@router.post('/create', response_model=Token_Pydantic)
async def create_token(token: TokenIn_Pydantic):
    unique_hash = get_random_string()
    # TODO me
    tx_hash = 'some_plug_' + get_random_string(5)
    token_obj = await Token.create(
        unique_hash=unique_hash,
        tx_hash=tx_hash,
        **token.dict()
    )
    return await Token_Pydantic.from_tortoise_orm(token_obj)
