from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello Fowjia"}
@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name}"}
from pydantic import BaseModel
tasks=[]
class Task(BaseModel):
    title: str
    done: bool = False
@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"message": "Task added", "total": len(tasks)}
@app.get("/tasks")
def get_tasks():
    return tasks
@app.delete("/tasks/{index}")
def delete_task(index: int):
    if index < 0 or index >= len(tasks):
        return {"error": "Task not found"}
    removed = tasks.pop(index)
    return {"message": "Task deleted", "task": removed}
@app.put("/tasks/{index}")
def update_task(index: int, task: Task):
    if index < 0 or index >= len(tasks):
        return {"error": "Task not found"}
    tasks[index] = task
    return {"message": "Task updated", "task": task}