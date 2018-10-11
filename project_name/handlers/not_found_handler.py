import tornado.web

class NotFoundHandler(tornado.web.RequestHandler):
    """
        This handler overides the default tornado Not Found Handler
        and allows to customize the returned page.
    """
    def prepare(self):  # for all methods
        self._reason = "Page not found :´("
        self.write_error(404)