from time import time
from datetime import datetime

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
        super(Application, self).__init__(routes, **settings)
        self.up_time = int(time())
        self.up_time_iso = datetime.now().isoformat(' ')
        self.request_counter = 0
