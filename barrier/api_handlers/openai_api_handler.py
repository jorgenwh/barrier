import os
from openai import OpenAI
from ..responses import create_success_response_object


class OpenAiApiHandler():
    def __init__(self):
        self._client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def prompt_text_completion_model(self, parameters: dict) -> dict:
        model = parameters["model"]
        messages = parameters["messages"]
        response = self._client.chat.completions.create(
                model=model,
                messages=messages,
        )
        completion = response.choices[0].message.content
        return create_success_response_object(completion)

    def prompt_image_generation_model(self, parameters):
        model = parameters["model"]

        if model == "dall-e-2":
            response = self._client.images.generate(
                    model=model,
                    prompt=parameters["prompt"],
                    size=parameters["size"],
            )
                
        elif model == "dall-e-3":
            response = self._client.images.generate(
                    model=model,
                    prompt=parameters["prompt"],
                    size=parameters["size"],
                    quality=parameters["quality"],
                    n=1,
            )

        image_url = response.data[0].url
        return create_success_response_object(image_url)

