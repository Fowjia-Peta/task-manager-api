# Task Manager API

A simple REST API built with FastAPI to manage tasks (CRUD operations).

## Features
- Add a task (POST /tasks)
- View all tasks (GET /tasks)
- Update a task (PUT /tasks/{task_id})
- Delete a task (DELETE /tasks/{task_id})

## Tech Stack
- Python
- FastAPI
- Pydantic
- Uvicorn
- SQLAlchemy
- SQLite

## How to Run
1. Install dependencies: pip install fastapi uvicorn sqlalchemy
2. Start the server: uvicorn main:app --reload
3. Open the docs: http://127.0.0.1:8000/docs

## Task Format
```json
{
  "title": "Learn FastAPI",
  "done": false
}