from fastapi import FastAPI, requests
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class test(BaseModel):
    data:str  
    timestamp:str

@app.post('/')
async def home(requests:test):
    if (requests.data=="hello"):
        if(requests.timestamp=="10"):
            return "status:200\nmessage:data saved successfuly"
        return "status:203\nmessage:error in storing data(wrong timestamp)"
    return "status:203\nmessage:error in storing data(wrong data)"
