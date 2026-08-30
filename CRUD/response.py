# # response model :
# response validation 
# hide sensitive data 
# output formatting

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str
    
class UserResponse(BaseModel): #sending only data which we want to send and hiding sensitive data 
    name:str
    age:int


@app.get("/user",response_model=UserResponse)
def get_user():
    return{
        "name":"Mohit",
        "age":24,
        "password":"123456"
    }
    