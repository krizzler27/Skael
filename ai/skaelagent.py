from ai.llmservices import LLMServices
class SkaelAgent:

    def __init__(self):
        self.llm = LLMServices()

    def parse_job(self, JOB_DESCRIPTION):
        prompt = self.llm.load_prompt('extractor-prompt', INPUT_CONTENT=JOB_DESCRIPTION, INPUT_TYPE=JOB_DESCRIPTION)
        response = self.llm.invoke_llm(prompt)
        return self.llm.clean_json(response.content)

    def parse_resume(self, USER_RESUME):
        prompt = self.llm.load_prompt('extractor-prompt', INPUT_CONTENT=USER_RESUME, INPUT_TYPE=USER_RESUME)
        response = self.llm.invoke_llm(prompt)
        return self.llm.clean_json(response.content)

    def analyze_match(self, AI_JD, AI_RESUME):
        prompt = self.llm.load_prompt('analyze-match-prompt', EXTRACTED_JOB_DATA=AI_JD, EXTRACTED_USER_DATA=AI_RESUME)
        response = self.llm.invoke_llm(prompt)
        return self.llm.clean_json(response.content)

    def resume_rewrite(self, AI_JD, AI_RESUME, AI_ANALYSIS):
        prompt = self.llm.load_prompt('resume-rewrite-prompt', JOB_JSON=AI_JD, RESUME_JSON=AI_RESUME, ANALYSIS_JSON=AI_ANALYSIS)
        response = self.llm.invoke_llm(prompt)
        return self.llm.clean_json(response.content)

    def resume_review(self, AI_REWRITE ,AI_JD):
        prompt = self.llm.load_prompt('resume-review-prompt', JOB_JSON=AI_JD, RESUME_REWRITE_JSON=AI_REWRITE)
        response = self.llm.invoke_llm(prompt)
        return self.llm.clean_json(response.content)