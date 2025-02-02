from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from src.database.session import get_db
from src.services.student_service import get_student_questions, get_student_questions_for_all_students
from src.schemas.student import StudentQuestionSchema
from typing import Optional
from datetime import datetime

router = APIRouter()

@router.get("/students/{student_id}/questions", response_model=List[StudentQuestionSchema])
def read_student_questions(student_id: int, db: Session = Depends(get_db)):
    return get_student_questions(db, student_id)

@router.get("/students/questions", response_model=List[StudentQuestionSchema])
def read_all_students_questions(
    since: Optional[datetime] = Query(None, description="Optional. Filter questions attempted after this date."),
    db: Session = Depends(get_db)
):
    """
    Returns all StudentQuestion records from the database.
    If 'since' is provided, returns only those records whose attempted_at >= since.
    """
    return get_student_questions_for_all_students(db, since)