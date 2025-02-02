from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.bedrock_service import bedrock_service

router = APIRouter()

class ClaudeRequest(BaseModel):
    prompt: str

@router.post("/claude/generate")
async def generate_claude_response(request: ClaudeRequest):
    response = await bedrock_service.generate_response(request.prompt)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])
    return {"response": response}
