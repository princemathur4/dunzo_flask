class RootException(Exception):
    def __init__(self, internal_err_message=None):
        if internal_err_message is not None:
            self.internal_err_message = internal_err_message

    internal_err_message = "Internal error occurred"
    http_code = 500


class InvalidInputParamter(RootException):
    internal_err_message = "Invalid input params provided"
    err_message = "Something went wrong"


class InvalidRequestPayload(RootException):
    internal_err_message = "Invalid request payload"
    err_message = "Invalid request payload"
    http_code = 400


class NoRecordsFound(RootException):
    internal_err_message = "No records found"
    err_message = "No records found"
    http_code = 404


class AddToCartError(RootException):
    internal_err_message = "Error occurred while adding to cart"
    err_message = "Error occurred while adding to cart"
