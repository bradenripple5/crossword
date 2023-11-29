from fastapi import FastAPI
import json

app = FastAPI()
with open("example.json") as f:
    data = json.loads(f.read())

@app.get("/")
async def root():
    return data #{"message": "Hello World"}
