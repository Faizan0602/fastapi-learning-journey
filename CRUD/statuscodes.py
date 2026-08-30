# Status Codes & Responses :

# . HTTP status codes
# . Custom responses
# . Error handling basics


from fastapi import FastAPI,status,HTTPException

app = FastAPI()

@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return{
        "message":"user created"
    }

#custom responses

@app.get("/user")
def get_user():
    return{
        "Status":"Success",
        "Message":"user fetched",
        "data":{
            "name":"faizan",
            "age":24
        }
        
    }

#exception handling

@app.get("/users/{user_id}")

def get_user(user_id:int):
    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail="USER NOT FOUND !"
        )
    return{
        "id":1,
        "name":"Faizan"
    }