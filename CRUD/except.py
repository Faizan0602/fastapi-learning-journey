# FastAPI Exception Handling
# See diagram: D:\AI PROJECTS\FAST API\CRUD\ChatGPT Image Aug 30, 2026, 06_53_17 PM.png






# Exception Handling

# . HTTPException
# . Custom exceptions
# . Global error handler


from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse

app = FastAPI()

# @app.get("/users{user_id}")

# def get_user(user_id:int):
#     if user_id!=1:
#         raise HTTPException(
#             status_code=404,
#             detail="user not found"
#         )
#     return{
#         "id":1,
#         "name":"faizan"
#     }
    
    
#CUSTOM EXP

class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name=name
        
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request:Request,exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"user{exc.name} not found"
        }
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name!="Faizan":
        raise UserNotFoundException(name)
    return{
        "name":name 
    }
    
# Problem

# Right now FastAPI doesn't know how to handle:

# UserNotFoundException

# So you'll get an internal server error (500).
# That's why we need a Global Exception Handler.

#code is above after user not found exception handling 






