from .openai_api_handler import OpenAiApiHandler
from .anthropic_api_handler import AnthropicApiHandler
from ..responses import (
    create_error_response_object,
)
from ..models.models_info import (
  SUPPORTED_TEXT_COMPLETION_MODELS,
  TEXT_COMPLETION_MODEL_VENDOR_MAP,
  SUPPORTED_IMAGE_GENERATION_MODELS,
  IMAGE_GENERATION_MODEL_VENDOR_MAP
)


class ApiHandler:
    def __init__(self):
        self._openai_api_handler = OpenAiApiHandler()
        self._anthropic_api_handler = AnthropicApiHandler()

    def prompt_text_completion_model(self, parameters):
        if "model" not in parameters:
            return create_error_response_object("'model' field not found in parameters")

        model = parameters["model"]
        if model not in SUPPORTED_TEXT_COMPLETION_MODELS:
            return create_error_response_object(
                "'" + model + "' is not a supported model for text completion")

        # more asserts? and should they even be here
        pass

        vendor = TEXT_COMPLETION_MODEL_VENDOR_MAP[model]
        if vendor == "openai":
            return self._openai_api_handler.prompt_text_completion_model(parameters)
        elif vendor == "anthropic":
            return self._anthropic_api_handler.prompt_text_completion_model(parameters)
        else:
            return create_error_response_object(
                "Prompting vendor '" + vendor + "' for text completion is not supported")

    def prompt_image_generation_model(self, parameters):
        if "model" not in parameters:
            return create_error_response_object("'model' field not found in parameters")

        model = parameters["model"]
        if model not in SUPPORTED_IMAGE_GENERATION_MODELS:
            return create_error_response_object(
                "'" + model + "' is not a supported model for image generation")

        # more asserts? and should they even be here
        pass

        vendor = IMAGE_GENERATION_MODEL_VENDOR_MAP[model]
        if vendor == "openai":
            return self._openai_api_handler.prompt_image_generation_model(parameters)
        else:
            return create_error_response_object(
                "Prompting vendor '" + vendor + "' for image generation is not supported")
