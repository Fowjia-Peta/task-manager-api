from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class Task(BaseModel):
    title: str
    done: bool = False


tasks: list[Task] = []


@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"index": len(tasks) - 1, "task": task}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.put("/tasks/{index}")
def update_task(index: int, task: Task):
    if index < 0 or index >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[index] = task
    return task


@app.delete("/tasks/{index}")
def delete_task(index: int):
    if index < 0 or index >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    removed = tasks.pop(index)
    return {"deleted": removed}
