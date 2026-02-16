from fastapi import APIRouter
from schemas import AssessmentCreate
from database import supabase

router = APIRouter(prefix="/assessment", tags=["Assessment"])

def calculate_score(answers):
    score = 0
    for ans in answers:
        if ans == "A":
            score += 2
        elif ans == "B":
            score += 1

    if score >= 18:
        risk = "Good"
    elif score >= 10:
        risk = "OK"
    else:
        risk = "Bad"

    return score, risk

@router.post("/")
async def submit_assessment(data: AssessmentCreate):

    score, risk = calculate_score(data.answers)

    supabase.table("assessments").insert({
        "name": data.name,
        "email": data.email,
        "answers": data.answers,
        "score": score,
        "risk_level": risk
    }).execute()

    return {
        "score": score,
        "risk_level": risk
    }