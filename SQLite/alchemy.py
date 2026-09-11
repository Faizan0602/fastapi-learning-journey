from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from sqlalchemy import Column,Integer,String
from fastapi import FastAPI,Depends

app =FastAPI()

#DATABSE URL
DATABASE_URL = "sqlite:///./test.db"

#ENGINE CREATE (DB CONNECTION)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

#SESSION(DB OPERATIONS KE LIYE)
sessionLocal =sessionmaker(bind=engine)

#BASE (MODEL KE LIYE)
Base = declarative_base()

#TABLE (MODEL CREATE)
class Todo(Base):
    __tablename__="todos"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    completed=Column(String)

#TABLE CREATE  
Base.metadata.create_all(bind=engine)

#DEPENDENCY (DB SESSION PROVIDE KAREGA)
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
    
# API    
@app.get("/")
def home(db:Session=Depends(get_db)):
    return{
        "message":"DB CONNECTED SUCCESSFULLY"
    }
            