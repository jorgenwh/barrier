SUPPORTED_MODELS = [
  "gpt-3.5-turbo",
  "gpt-4-turbo-preview",
  "dall-e-2",
  "dall-e-3",
  "claude-3-opus-20240229",
]

SUPPORTED_TEXT_COMPLETION_MODELS = [
  "gpt-3.5-turbo",
  "gpt-4-turbo-preview",
  "claude-3-opus-20240229",
]

SUPPORTED_IMAGE_GENERATION_MODELS = [
  "dall-e-2",
  "dall-e-3",
]

MODEL_VENDOR_MAP = {
        "gpt-3.5-turbo": "openai",
        "gpt-4-turbo-preview": "openai",
        "dall-e-2": "openai",
        "dall-e-3": "openai",
        "claude-3-opus-20240229": "anthropic",
}

TEXT_COMPLETION_MODEL_VENDOR_MAP = {
        "gpt-3.5-turbo": "openai",
        "gpt-4-turbo-preview": "openai",
        "claude-3-opus-20240229": "anthropic",
}

IMAGE_GENERATION_MODEL_VENDOR_MAP = {
        "dall-e-2": "openai",
        "dall-e-3": "openai",
}

OPENAI_TEXT_COMPLETION_MODELS = ["gpt-3.5-turbo", "gpt-4-turbo-preview"]
OPENAI_IMAGE_GENERATION_MODELS = ["dall-e-2", "dall-e-3"]
ANTHROPIC_TEXT_COMPLETION_MODELS = ["claude-3-opus-20240229"]