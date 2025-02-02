from fastapi import FastAPI
from src.routes import student, claude

app = FastAPI(title="Backend Service")

app.include_router(student.router, prefix="/api", tags=["Students"])
app.include_router(claude.router, prefix="/api", tags=["Claude"])

@app.get("/")
def health_check():
    return {"message": "Backend is running!"}
