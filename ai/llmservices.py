from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import json
import re
import os

class LLMServices:
    def __init__(self):
        self.llm_model = ChatGoogleGenerativeAI(
            model='gemini-2.0-flash',
            temperature=0.4
        )

        self.prompt_folder = r'ai\prompts'

    def invoke_llm(self, prompt):
        response = self.llm_model.invoke(prompt)
        return response

    def clean_json(self, result, for_llm=True):
        """Clean and parse JSON response from LLM"""
        result = result.strip()
        if result.startswith("```json"):
            result = re.sub(r"```json\s*|\s*```", "", result).strip()
        try:
            if for_llm:
                return json.dumps(json.loads(result), ensure_ascii=False)
            else:
                return json.loads(result)
        except Exception:
            raise ValueError(f"LLM output could not be parsed as expected:\n{result}") 

    def load_prompt(self, prompt_name, **values):
        prompt_path = os.path.join(self.prompt_folder, f"{prompt_name}.txt")
        with open(prompt_path, 'r') as f:
            template = f.read()
            prompt = PromptTemplate.from_template(template)
            prompt = prompt.format(**values)
        return prompt