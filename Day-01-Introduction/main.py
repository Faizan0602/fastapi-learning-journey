# from fastapi import FastAPI

# app = FastAPI()


# #home route
# @app.get("/")

# def home():
#     return{"message" : "This is home page"}

# #about route
# @app.get("/about")

# def about():
#     return{"message" : "This is about page"}

# #user route
# @app.get("/users")

# def users():
#     return{
#         "users" : ["Faizan" , "Alex" , "Ahmad"]
#     }
    
# dynamic routes and path parameters : 

from fastapi import FastAPI

app = FastAPI()

#users route
@app.get("/users/{user_id}")   #path parameter

def get_user(user_id:int):
    return{"user_id": user_id}

