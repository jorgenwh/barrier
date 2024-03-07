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
def prompt_chat():
    data = request.get_json()
    model = data["model"]
    messages = data["messages"]

    if model in ["gpt-3.5-turbo", "gpt-4-turbo-preview"]:
        print("prompting " + model)
        completion = openai_api_handler.prompt_text_model(
                model=model,
                messages=messages
        )
    elif model in ["claude-3-opus-20240229"]:
        print("prompting " + model)
        completion = anthropic_api_handler.prompt_text_model(
                model=model,
                messages=messages
        )
    else:
        return jsonify({"error": "Model not found"})

    print("completion: " + completion)
    return jsonify({"response": completion})


if __name__ == "__main__":
    app.run(debug=True)
