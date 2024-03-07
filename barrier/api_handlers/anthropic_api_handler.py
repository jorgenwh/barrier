import os
from anthropic import Anthropic


class AnthropicApiHandler():
    def __init__(self):
        self._client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def prompt_text_model(self, model, messages):
        response = self._client.messages.create(
                model=model,
                max_tokens=1024,
                messages=messages,
        )
        completion = response.content[0].text
        return completion

