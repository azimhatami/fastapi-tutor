from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse


app = FastAPI()


@app.get('/portal')
async def get_teleport(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url='https://w3schools.com/')
    return JSONResponse(content={'message': 'Here\'s your interdimensional portal.'})
