from fastapi import FastAPI
from enum import Enum
app = FastAPI()


class ModelName(str, Enum):
    john = "john"
    rick = "rick"
    morty = "morty"

# 127.0.0.1:8000
@app.get('/')
# @app.options()
# @app.head()
# @app.patch()
# @app.trace()
async def root():
    return {'message': 'Hello World'}

# 127.0.0.1:8000/item/codepedia
@app.get('/item/{para}')
async def welcome(para : str):
    return {'welcome' : para }

# 127.0.0.1:8000/users/anakin

@app.get('/users')
async def members():
    return ["Rick", "Morty"]


@app.get('/users/starwars/{force}/{dark}')
async def members3(force, dark):
    return [force , dark]


@app.get('/users/dc/{u}')
async def members2(u : str):
    return ["batman", u]

@app.get("/models/{model_name}")
async def getModel(model_name : ModelName):
    if model_name is ModelName.john:
        return {"model_name" : model_name, "message": f"Welcom back mr {model_name.name}"}

    if model_name.value == "rick":
        return {"model_name": model_name, "message":"my name is RICK..."}


fake_db = [
    {"item_name":"FOO"},
    {"item_name":"BAR"},
    {"item_name":"BAZ"}
]

# 127.0.0.1:8000/myitems/?skip=0&limit=10
@app.get("/myitems/")
async def myitems_read(skip : int = 0, limit : int = 10):
    return fake_db[skip : skip + limit]