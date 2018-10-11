from time import time
from datetime import datetime
from handlers.not_found_handler import NotFoundHandler
import tornado.web

class Application(tornado.web.Application):
    """
    Tornado extended application class
    """
    def __init__(self, routes: list, autoreload: bool):
        settings = dict(
            debug=True,
            autoreload=autoreload
        )
        super(Application, self).__init__(routes, **settings, default_handler_class=NotFoundHandler)
        self.up_time = int(time())
        self.up_time_iso = datetime.now().isoformat(' ')
        self.request_counter = 0
        