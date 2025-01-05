from fastapi import FastAPI, requests
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class test(BaseModel):
    task: str
    status : str
    timestamp : str

@app.post('/')
async def home(requests:test):
        # return requests.task , requests.status , requests.timestamp
        return requests
        