from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.post("/create-todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message": "TODO added","data":todo}

@app.get("/get-todo")
def get_todo():
    return todos

@app.get("/get-todo/{todo_id}")
def getTodoBasedOnId(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo doesn't exist")

@app.put("/update-todo/{todo_id}")
def update_todo(todo_id:int, updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return{
                "message":"Data Updated",
                "data": updated_todo
            }
    raise HTTPException(status_code=404, detail="Todo not found")



@app.delete("/delete-todo/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message" : "Data Deleted"}
    raise HTTPException(status_code=404,detail="Todo not found") 


