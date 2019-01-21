"""
Create errors and stores API known errors
"""

class Errors():
    """
    Handles all information we need to create an error
    """
    def __init__(self, error_name: str, error_message: str, http_status_code: int):
        self.error_message = error_message
        self.error_code = error_name
        self.http_status_code = http_status_code

    @property
    def json(self) -> dict:
        """
        Creates an error dict to be returned by our API
        """
        error_json = {
            "error_code" : self.error_code,
            "error_message" : self.error_message
        }
        return error_json

MALFORMED_JSON = Errors("MALFORMED_JSON",
                        "The JSON could not be understood by the server due to malformed syntax.",
                        400)

RESOURCE_NOT_FOUND = Errors("RESOURCE_NOT_FOUND", 'The requested resource was not found.', 404)

METHOD_NOT_ALLOWED = Errors("METHOD_NOT_ALLOWED",
                            "This method is not allowed. Please check API docs.", 405)

#We define 'field' as a key of a JSON passed in request's body
MISSING_FIELD = lambda key: Errors("MISSING_FIELD",
                                   "Field {} is missing or has a null value.".format(key), 400)

INVALID_FIELD = lambda key: Errors("INVALID_FIELD",
                                   "Field '{}' is invalid for this request.".format(key), 400)

INVALID_FIELD_TYPE = lambda key1, key2: Errors("INVALID_FIELD_TYPE",
                                               "Type of field '{}' is invalid nd must be {}.".format(key1, key2), 400)

#We define 'parameter' as a value in request's URL
MISSING_PARAMETER = lambda key: Errors("MISSING_PARAMETER",
                                       "Parameter '{}' is missing or has a null value.".format(key), 400)

INVALID_PARAMETER = lambda key: Errors("INVALID_PARAMETER",
                                       "Parameter '{}' is invalid for this request.".format(key), 400)

INVALID_PARAMETER_TYPE = lambda key1, key2: Errors("INVALID_PARAMETER TYPE",
                                                   "Type of parameter '{}' is invalid and must be {}.".format(key1, key2), 400)

DATABASE_ERROR = Errors("DATABASE_ERROR",
                        "Something went wrong in our database. Please report this error.", 500)

UNAUTHORIZED = Errors("UNAUTHORIZED",
                      "User not authorized to perform this action.", 403)

UNAUTHENTICATED = Errors("UNAUTHENTICATED",
                         "User not authenticated. Please, perform an authentication before execute this action.", 401)
