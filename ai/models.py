from typing import TypedDict

class SkaelState(TypedDict):

    job_description: str
    user_resume: str

    extracted_job_data: str
    extracted_user_data: str

    analyze: str