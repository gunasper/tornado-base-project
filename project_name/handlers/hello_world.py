from .base import BaseHandler

class HelloWorldHandler(BaseHandler):
    """
    Handler implementing GET, POST, PUT and DELETE methods
    """

    async def get(self):
        """
        GET
        """
        self.write("Hello World!")
        pass

    async def post(self):
        """
        POST
        """
        pass

    async def put(self):
        """
        PUT
        """
        pass

    async def delete(self):
        """
        DELETE
        """
        pass
