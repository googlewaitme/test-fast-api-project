from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Token(models.Model):
    id = fields.IntField(pk=True)
    unique_hash = fields.CharField(max_length=20, unique=True)
    tx_hash = fields.CharField(max_length=256)
    media_url = fields.CharField(max_length=256)
    owner = fields.CharField(max_length=256)


Token_Pydantic = pydantic_model_creator(Token, name='Token')
TokenIn_Pydantic = pydantic_model_creator(
    Token, name='TokenIn',
    exclude=("tx_hash", "unique_hash"),
    exclude_readonly=True
)
