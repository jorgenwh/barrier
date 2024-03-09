
def create_success_response_object(response: str) -> dict:
    return {
        "status": "success",
        "response": response
    }

def create_error_response_object(response: str) -> dict:
    return {
        "status": "error",
        "response": response
    }
