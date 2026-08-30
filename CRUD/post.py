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

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# #input validation using pydantic
# class User(BaseModel):
#     name:str                   
#     age:int

# @app.post("/create-user")
# def create_user(user:User):
#     return{
#         "message" : "User Created",
#         "data" : user
#     }
    
# pydantic model ----> ye ek schema structure hota hai jo define karta hai data ka format kaisa hoga
# user ke pass kitni field honi chahiye ye pydantic model define karta hai 
#pydantic model mai aapne bataya user k pass name,age,email honi chahiye to yhi 3 cheezein hogi jo hamne pehle se define kari hui hai iske alawa aur kuch nhi hoga
#to pydantic model mai hamei pehle se hi field define karni hoti hai isi hisaab se hum model create karte hai

#1 Creating schema

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     email:str

# @app.post("/create_user")

# def create_user(user:User):
#     return{
#         "message" : "user created",
#         "data": user
#     }
    
    
#Nested Models 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/create_user")
def create_user(user:User):
    return{
        "message":"USER CREATED",
        "data":user
    }