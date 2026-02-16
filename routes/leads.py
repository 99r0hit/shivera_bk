from fastapi import APIRouter, Request
from schemas import LeadCreate
from database import supabase

router = APIRouter(prefix="/leads", tags=["Leads"])

@router.post("/")
async def create_lead(data: LeadCreate, request: Request):

    service = supabase.table("services") \
        .select("*") \
        .eq("name", data.service) \
        .execute()

    if not service.data:
        return {"error": "Service not found"}

    service_id = service.data[0]["id"]

    supabase.table("leads").insert({
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "service_id": service_id,
        "message": data.message,
        "ip_address": request.client.host,
        "user_agent": request.headers.get("user-agent")
    }).execute()

    return {"message": "Lead created successfully"}