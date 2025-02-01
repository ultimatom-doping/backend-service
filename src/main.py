from fastapi import FastAPI
from src.routes import quiz, student

app = FastAPI(title="Backend Service")

app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(student.router, prefix="/student", tags=["Student"])

@app.get("/")
def health_check():
    return {"message": "Backend is running!"}
