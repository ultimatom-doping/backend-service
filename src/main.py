from fastapi import FastAPI
from src.routes import student

app = FastAPI(title="Backend Service")

app.include_router(student.router, prefix="/api", tags=["Students"])

@app.get("/")
def health_check():
    return {"message": "Backend is running!"}
