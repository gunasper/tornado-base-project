import sys
import tornado.ioloop
import tornado.httpserver
from tornado.log import enable_pretty_logging
from routes import ROUTES
from application import Application

PORT = 5000
AUTORELOAD = True

if __name__ == "__main__":
    
    enable_pretty_logging()
    args = sys.argv
    args.append("--log_file_prefix=my_app.log")
    tornado.options.parse_command_line(args)

    app = Application(ROUTES, autoreload=AUTORELOAD)
    
    try:
        server = tornado.httpserver.HTTPServer(app)
        server.bind(PORT)
        if AUTORELOAD:
            print("starting single process server")
            server.start(1)
        else:
            print("starting multiple process server")
            server.start(0)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()