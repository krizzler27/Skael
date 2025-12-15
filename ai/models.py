from typing import TypedDict
from pydantic import BaseModel

# Used For Langraph Orchestration
class SkaelState(TypedDict):

    job_description: str
    user_resume: str
    extracted_job_data: str
    extracted_user_data: str
    analyze: str

class Analyze(BaseModel):
    job_description: str
    user_resume: str