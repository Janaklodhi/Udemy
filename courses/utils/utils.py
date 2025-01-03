def custom_response(status, message, data=None, errors=None):
    return {
        "status": status,
        "message": message,
        "data": data,
        "errors": errors,
    }
