import os
from anthropic import Anthropic
from ..responses import create_success_response_object


class AnthropicApiHandler():
    def __init__(self):
        self._client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def prompt_text_completion_model(self, parameters: dict) -> dict:
        model = parameters["model"]
        messages = parameters["messages"]
        response = self._client.messages.create(
                model=model,
                max_tokens=1024,
                messages=messages,
        )
        completion = response.content[0].text
        return create_success_response_object(completion)

