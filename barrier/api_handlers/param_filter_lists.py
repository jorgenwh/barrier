
MODEL_PARAM_LIST = {
        "dall-e-2": ["size"],
        "dall-e-3": ["size", "quality"],
}


def filter_parameters(model, parameters):
    if model not in MODEL_PARAM_LIST:
        return None

    filtered_parameters = {}

    for p in parameters:
        if p in MODEL_PARAM_LIST[model]:
            filtered_parameters[p] = parameters[p]

    return filtered_parameters
