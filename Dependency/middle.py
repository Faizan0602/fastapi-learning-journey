# Middleware

# . What is middleware?
# . Logging middleware
# . Request/response flow

from fastapi import FastAPI,Request
import time

app = FastAPI()

#middle ware flow :

# @app.middleware("http")
# async def my_middleware(request:Request,call_next):
#     print("Request Recieved")
#     response=await call_next(request)
#     print("Response Sent")
#     return response

#logging middleware (kitna time lagta hai ek api ko request response bhejne mai)
#real world use case 

@app.middleware("http")
async def logging_time(request:Request,call_next):
    start_time=time.time()
    responce = await call_next(request)
    process_time=time.time()-start_time
    print(f"path:{request.url.path} | Time: {process_time}")

    return responce