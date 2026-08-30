# path+query+body combo 
# mix all inputs 
# real-world api structure 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users=[]

class User(BaseModel):
    name:str
    age:int
    
@app.post("/user")
def create_user(user:User):
    users.append(user)
    return{
        "message":"user created",
        "data":user
    }
@app.put("/user/{user_id}")
def updated_user(user_id:int,user:User,notify:bool=True):
    if user_id<len(users):
        users[user_id]=user
        
        return{
            "message":"user updated",
            "notify":notify,
            "data":user
        }
    return {"message":"User not found"}

@app.get("/user")
def fetch_user():
    return users