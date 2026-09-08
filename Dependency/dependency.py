# Dependency Injection

# . What is Depends()
# . Reusable logic
# . Auth example intro


from fastapi import FastAPI,Depends,Header,HTTPException,status

app = FastAPI()

# def common_logic():
#     return{
#         "message":"Common Logic Executed"
#     }

# @app.get("/home")
# def home(data=Depends(common_logic)):
#     return data

# resuable logic example : 

# def get__cuurent_user():
#     return{
#         "name":"Faizan"
#     }
    
# @app.get("/profile")
# def profile(user=Depends(get__cuurent_user)):
#     return user

# @app.get("/dashboard")
# def dashboard(user=Depends(get__cuurent_user)):
#     return user

# . Auth example

def verify_token(token:str=Header(None)):
    if token!="mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="unauthorised"
            
        )
    return{
        "user" :"Authorised user"
    }

@app.get("/secure_data")
def secure_data(user=Depends(verify_token)):
    return{
        "message":"secure data accessed",
        "user":user
    }