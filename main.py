from flask import Flask, json, request, jsonify
from flask_cors import CORS
import logging
from datetime import datetime

from barrier import OpenAiApiHandler, AnthropicApiHandler


app = Flask(__name__)
CORS(app)

openai_api_handler = OpenAiApiHandler()
anthropic_api_handler = AnthropicApiHandler()

logging.basicConfig(
        filename="logs/" + str(datetime.now()) + "_session.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
)

@app.route("/")
def root():
    return "Nothing here"


@app.route("/chat_prompt/", methods=["POST"])
def chat_prompt():
    data = request.get_json()

    model = data["model"]
    messages = data["messages"]

    logging.info("\33[1m--- Received chat prompt with parameters ---\33[0m")
    logging.info("model=" + str(model))
    logging.info("messages=" + str(messages))

    if model in ["gpt-3.5-turbo", "gpt-4-turbo-preview"]:
        completion = openai_api_handler.prompt_text_model(
                model=model,
                messages=messages
        )
    elif model in ["claude-3-opus-20240229"]:
        completion = anthropic_api_handler.prompt_text_model(
                model=model,
                messages=messages
        )
    else:
        return jsonify({"error": "Model not found"})

    logging.info("completion=" + str(completion))
    return jsonify({"response": str(completion)})

@app.route("/image_prompt/", methods=["POST"])
def image_prompt():
    data = request.get_json()

    model = data["model"]
    prompt = data["prompt"]
    parameters = data["parameters"]

    logging.info("\33[1m--- Received image prompt with parameters ---\33[0m")
    logging.info("model=" + str(model))
    logging.info("parameters=" + str(parameters))
    logging.info("prompt=" + str(prompt))

    if model in ["dall-e-3"]:
        response = openai_api_handler.prompt_image_model(
                model=model,
                prompt=prompt,
                parameters=parameters,
        )
    else:
        return jsonify({"error": "Model not found"})

    logging.info("response=" + str(response))
    return jsonify({"response": str(response)})


if __name__ == "__main__":
    app.run(host="192.168.0.87", port=5000)
