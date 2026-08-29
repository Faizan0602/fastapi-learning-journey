#leanring crud operation using TO-DO application project

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title:str
    completed:bool

@app.post("/todos")

def create_todo(todo:Todo):
    todos.append(todo)
    return{
        "message":"TODO ADDED",
        "data":todo
    }
    

@app.get("/todos")
def get_todos():
    return todos

#to fetch single data through id

@app.get("/todos/{todo_id}")  # path params
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    return{"error todo not found"}

#updating data 

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index, todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return{
                "message" : "todo updated",
                "data":updated_todo
            }
    return{"error no todo found"}

@app.delete("/todos/{todo_id}")

def delete_todo(todo_id:int):
     for index, todo in enumerate(todos):
         if todo.id==todo_id:
             todos.pop(index)
             return{"message": "data deleted ",}
     return{"error : Todo not found"}