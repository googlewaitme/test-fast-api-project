from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise

from routers import tokens

from loader import w3, contract


app = FastAPI()

app.include_router(tokens.router)


@app.get('/')
async def send_hello_world():
    return {'response': "Hello World!"}


register_tortoise(
    app,
    db_url="sqlite://:memory:",
    modules={"models": ["models.token"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
