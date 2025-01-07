from fastapi import FastAPI, requests
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class test(BaseModel):
    data:str  
    timestamp:str

@app.post('/save-data')
async def home(requests:test):
    if (requests.data=="hello"):
        if(requests.timestamp=="10"):
            return {"status":200 , "message":"data saved successfully"} 
        return {"status":203 , "message":"error in storing data(wrong timeline)"}
    return {"status":203 , "message":"error in storing data(wrong data)"}