from ai.llmservices import LLMServices
from langgraph.graph import StateGraph, START, END
from ai.models import SkaelState

class SkaelAgent:

    def __init__(self):
        self.llm = LLMServices()
    
    def parse_job(self, state: SkaelState):
        prompt = self.llm.load_prompt('ats-extractor-prompt', JOB_DESCRIPTION=state["job_description"])
        response = self.llm.invoke_llm(prompt)
        return {"extracted_job_data" : self.llm.clean_json(response.content)}
    
    def parse_resume(self, state: SkaelState):
        prompt = self.llm.load_prompt('resume-extractor-prompt', USER_RESUME=state["user_resume"])
        response = self.llm.invoke_llm(prompt)
        return {"extracted_user_data" : self.llm.clean_json(response.content)}

    def analyze_match(self, state: SkaelState):
        prompt = self.llm.load_prompt('analyze-match-prompt', EXTRACTED_JOB_DATA=state["job_description"], EXTRACTED_USER_DATA=state["user_resume"])
        response = self.llm.invoke_llm(prompt)
        return {"analyze" : self.llm.clean_json(response.content)}

    # Use this Orchestrator to run whole workflow as Single process
    def orchestrator(self, job_desc, user_resume):

        workflow = StateGraph(SkaelState)
        workflow.add_node("parse_job", self.parse_job)
        workflow.add_node("parse_resume", self.parse_resume)
        workflow.add_node("analyze_match", self.analyze_match)

        workflow.add_edge(START, "parse_job")
        workflow.add_edge("parse_job", "parse_resume")
        workflow.add_edge("parse_resume", "analyze_match")
        workflow.add_edge("analyze_match", END)

        graph = workflow.compile()
        res = graph.invoke(
            {
                "job_description":job_desc,
                "user_resume":user_resume
            }
        )

        return res