from fastapi import FastAPI

app = FastAPI()


#home route
@app.get("/")

def home():
    return{"message" : "This is home page"}

#about route
@app.get("/about")

def about():
    return{"message" : "This is about page"}

#user route
@app.get("/users")

def users():
    return{
        "users" : ["Faizan" , "Alex" , "Ahmad"]
    }