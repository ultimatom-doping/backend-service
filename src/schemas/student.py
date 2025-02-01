from pydantic import BaseModel
from datetime import datetime

class StudentQuestionSchema(BaseModel):
    id: int
    student_id: int
    question_id: int
    result: str
    attempted_at: datetime

    class Config:
        orm_mode = True
