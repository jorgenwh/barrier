from flask import Flask, json, request, jsonify
from flask_cors import CORS


from barrier import OpenAiApiHandler, AnthropicApiHandler


app = Flask(__name__)
CORS(app)

openai_api_handler = OpenAiApiHandler()
anthropic_api_handler = AnthropicApiHandler()


@app.route("/")
def root():
    return "Nothing here"


@app.route("/chat_prompt/", methods=["POST"])
def chat_prompt():
    data = request.get_json()

    model = data["model"]
    messages = data["messages"]

    print("--- Received chat prompt with parameters ---")
    print("model=" + model)
    print("messages=" + messages)

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

    print("completion=" + completion)
    return jsonify({"response": completion})

@app.route("/image_prompt/", methods=["POST"])
def image_prompt():
    data = request.get_json()

    model = data["model"]
    prompt = data["prompt"]
    parameters = data["parameters"]

    print("--- Received image prompt with parameters ---")
    print("model=" + model)
    print("parameters=" + parameters)
    print("prompt=" + prompt)

    if model in ["dall-e-3"]:
        completion = openai_api_handler.prompt_image_model(
                model=model,
                prompt=prompt,
                parameters=parameters,
        )
    else:
        return jsonify({"error": "Model not found"})

    return jsonify({"response": completion})


if __name__ == "__main__":
    app.run(debug=True)
