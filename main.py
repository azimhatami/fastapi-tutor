from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse


app = FastAPI()


@app.get('/teleport')
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url='https://w3schools.com/')
