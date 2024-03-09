import os
from openai import OpenAI


class OpenAiApiHandler():
    def __init__(self):
        self._client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def prompt_text_model(self, model, messages):
        response = self._client.chat.completions.create(
                model=model,
                messages=messages,
        )
        completion = response.choices[0].message.content
        return completion

    def prompt_image_model(self, model, prompt, parameters):
        response = self._client.images.generate(
                model=model,
                prompt=prompt,
                size=parameters["size"],
                quality=parameters["quality"],
                n=1,
        )
        image_url = response.data[0].url
        return image_url
