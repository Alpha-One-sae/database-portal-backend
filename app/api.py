from fastapi import FastAPI, requests
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class save(BaseModel): 
    timestamp:str
    data:str 

@app.post('/save-data')
async def home(requests:save):
    if (requests.timestamp=="12"):
        if(requests.data=="sanchi"):
            return {
                "status":"200",
                "message":"Data saved successfully"
            }
        return {
                "status":"203",
                "message":"Error in storing data"
            }
    return {
        "status" : "203",
        "message" : "Error in storing data"
    }