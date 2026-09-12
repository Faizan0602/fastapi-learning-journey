from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app =FastAPI()
load_dotenv()

#ALLOWED ORIGIN FOR FRONTEND URL 

origins=os.getenv("ORIGINS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, #allowing frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return{
        "message": "CORS ENABLED API"
    }