from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:8000
@app.get("/")
async def myfunc():
   return {"message":"hello world af API"}