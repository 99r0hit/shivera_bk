from pydantic import BaseModel
from typing import List, Optional

class LeadCreate(BaseModel):
    name: str
    email: str
    phone: str
    service: str
    message: Optional[str] = None

class AssessmentCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    answers: List[str]