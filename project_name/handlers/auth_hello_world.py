from .auth_handler import AuthHandler, authenticated_by_token

class AuthHelloWorldHandler(AuthHandler):
    """
    Handler implementing GET, POST, PUT and DELETE methods
    """
    @authenticated_by_token
    async def get(self):
        """
        GET is an authenticated method
        """
        self.write("Hello World GET!")

    @authenticated_by_token
    async def post(self):
        """
        POST is an authenticated method
        """
        self.write("Hello World POST!")

    async def put(self):
        """
        PUT isn't an authenticated method
        """
        pass

    async def delete(self):
        """
        DELETE isn't an authenticated method
        """
        pass
