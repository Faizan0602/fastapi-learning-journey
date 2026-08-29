#Request body -----> Data jo client backend ko bhejta hai 
#json ke format mai bhejta jata hai using post method 

# from fastapi import FastAPI

# app = FastAPI()

#normal working for understanding
# @app.post("/create-user")
# def create_user(name:str,age:int):
#     return{
#         "name":name,
#         "age":age
#     }


#real example of how json is returned

# @app.post("/create-user")
# def create_user(user:dict):
#     return{
#         "message" : "User Created",
#         "data" : user
#     }

# but in above example there is no validation everything is returned in json according to us like name should be in str and age in int
#for this we have pydantic

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#input validation
class User(BaseModel):
    name:str                   
    age:int

@app.post("/create-user")
def create_user(user:User):
    return{
        "message" : "User Created",
        "data" : user
    }