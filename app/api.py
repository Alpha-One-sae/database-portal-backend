from fastapi import FastAPI, requests, HTTPException, Header
from pydantic import BaseModel
from dotenv import load_dotenv
from pymongo import MongoClient
import os



load_dotenv()
app = FastAPI()

x_api_key = os.getenv("API_KEY")
uri = os.getenv("URI")

database = MongoClient(uri)
db = database["SAE"]
collection = db["Database"]

def verify_authkey(apikey: str):
    if apikey != x_api_key:
        raise HTTPException(status_code=403, detail= "not authentic request")

#Pay-Load ---------------
class testObj(BaseModel):
    test: str


class member(BaseModel):
    phoneNo: list
#----------- ------------------------

#Headers || Request ---------------------------
@app.post('/') #---Path---- ('/') single slash - root path
async def home(requests:testObj, x_api_key: str = Header(...)):
    verify_authkey(x_api_key)
    return requests.test

@app.post('/find-member')
async def find_member(requests:member, x_api_key: str = Header(...)):
    verify_authkey(x_api_key)

    #Logic for getting the particular member

    result = list(collection.find({"PHONE NO.": requests.phoneNo},{"_id":0}))

    return result

#---------------------------------