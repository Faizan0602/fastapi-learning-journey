#CRUD OPERATIONS USING SQL ALCHEMY


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from sqlalchemy import Column,Integer,String
from fastapi import FastAPI,Depends,HTTPException

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
    
# CREATE API    

@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
    todo=Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"TODO CREATED",
        "data":todo
    }


#READ API (ALL DATA AND BASED ON ID BOTH)

#READ ALL DATA 

@app.get("/todos")
def get_todos(todo_id=int ,db:Session=Depends(get_db)):
    todos=db.query(Todo).all()  #reading / getting all data 
    
    return{
        "Total":len(todos),
        "data":todos
    }

#read / get data by id
@app.get("/todos/{todo_id}")
def get_todo(todo_id=int,db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
        raise HTTPException(status_code=404,detail="todo not found")
    return todo

# UPDATE 
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
            raise HTTPException(status_code=404,detail="todo not found")
    
    todo.title=title
    db.commit()
    db.refresh(todo)
    return{
        "message":"updated",
        "data":todo
    }
    

#DELETE 

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
                raise HTTPException(status_code=404,detail="todo not found")
        
    db.delete(todo)
    db.commit()
    
    return{
        "message":"todo deleted",
        
    }
    