import tornado
from .base import BaseHandler
from commons.errors import Errors, UNAUTHENTICATED

class AuthHandler(BaseHandler):
    """
    Personalized logic to be used in Handlers that demands Authentication
    """
    def __init__(self, *args, **kwargs):
        super(AuthHandler, self).__init__(*args, **kwargs)

HEADER_TOKEN = 'abc'

def authenticated_by_token(method):
    """Authentication decorator using a token to be used in a method"""
    
    @tornado.gen.coroutine
    def authenticate(*args, **kw):
        """Checks if a user is authenticated or not based on a token passed in header"""
        handler = args[0]
        try:
            auth_header = handler.request.headers.get('Authorization', None)
            if auth_header:
                if auth_header == HEADER_TOKEN:
                    yield method(*args, **kw)
                else:
                    handler.write_error(UNAUTHENTICATED)
            else:
                handler.write_error(UNAUTHENTICATED)                
        except Exception as e:
            handler.write_error(UNAUTHENTICATED)

    return authenticate