from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.database.session import get_db
from src.services.student_service import get_student_questions
from src.schemas.student import StudentQuestionSchema

router = APIRouter()

@router.get("/students/{student_id}/questions", response_model=List[StudentQuestionSchema])
def read_student_questions(student_id: int, db: Session = Depends(get_db)):
    return get_student_questions(db, student_id)
