from fastapi import APIRouter, status
from ai.skaelagent import SkaelAgent
from ai.models import Analyze
router = APIRouter()

@router.post('/analyze', status_code=status.HTTP_200_OK, tags=['Skael'])
def analyze_ats(request: Analyze):
    ai = SkaelAgent()
    res = ai.orchestrator(request.job_description, request.user_resume)
    return res["analyze"]



