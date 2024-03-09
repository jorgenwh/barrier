from flask import Flask, json, request, jsonify
from flask_cors import CORS
import logging
from datetime import datetime

from barrier.api_handlers import ApiHandler
from barrier.responses import create_success_response_object, create_error_response_object

app = Flask(__name__)
CORS(app)

api_handler = ApiHandler()

logging.basicConfig(
        filename="logs/" + str(datetime.now()) + "_session.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("STARTING SERVER - " + str(datetime.now()))


@app.route("/")
def root():
    return None

@app.route("/prompt/", methods=["POST"])
def prompt():
    data = request.get_json()

    if "parameters" not in data:
        logging.error("server received no parameters")
        return create_error_response_object("server received no parameters")

    params = data["parameters"]
    logging.info("Received prompt request with parameters: " + str(params))

    if "type" not in params:
        logging.error("server received no prompt type")
        return create_error_response_object("server received no prompt type")

    prompt_type = params["type"]
    
    if prompt_type == "text-completion":
        response = api_handler.prompt_text_completion_model(params)
    elif prompt_type == "image-generation":
        response = api_handler.prompt_image_generation_model(params)
    else:
        logging.error("server received unknown prompt type: '" + prompt_type + "'")
        return create_error_response_object(
                "server received unknown prompt type: '" + prompt_type + "'")

    logging.info("Returning response: " + str(response))
    return response


if __name__ == "__main__":
    app.run(host="192.168.0.87", port=5000, debug=True)
