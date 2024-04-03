import json

from jinja2 import Environment, BaseLoader

from src.config import Config
from src.agents.llm import LLM

PROMPT = open("src/agents/search/prompt.jinja2", "r").read().strip()


class LeadParser:
    def __init__(self, base_model: str="gpt-4-0125-preview"):
        config = Config()
        # self.project_dir = config.get_projects_dir()
        
        self.llm = LLM(model_id=base_model)

    def render(
        self, conversation: str
    ) -> str:
        env = Environment(loader=BaseLoader())
        template = env.from_string(PROMPT)
        return template.render(
            conversation=conversation
        )

    def validate_response(self, response: str):
        response = response.strip().replace("```json", "```")
        
        if response.startswith("```") and response.endswith("```"):
            response = response[3:-3].strip()
        # print(response)
        try:
            response = json.loads(response)
            # print(response)
        except Exception as _:
            return False

        if "product" not in response:
            return False
        else:
            return response

    def execute(self, conversation: str) -> str:
        # print(conversation)
        prompt = self.render(conversation)
        # print(prompt)
        response = self.llm.inference(prompt)
        # print(response)
        
        valid_response = self.validate_response(response)
        # print("VALID RESPONSE:", valid_response)
        if not valid_response:
            print("Invalid response from the model, trying again...")
            return "Invalid response from the model, trying again..."
        
        # print("===" * 10)
        # print(valid_response)

        return valid_response
