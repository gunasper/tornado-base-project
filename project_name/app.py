import argparse
import sys
import tornado.ioloop
import tornado.httpserver
from tornado.log import enable_pretty_logging
from routes.routes import ROUTES
from application import Application


#custom args
parser = argparse.ArgumentParser()
parser.add_argument("--prod", action='store_true', help="Starts server in production mode")
parser.add_argument("--log_file_prefix", default='my_app.log', help="Select where log file will be saved")
args = parser.parse_args()

PORT = 5000
AUTORELOAD = not args.prod

#tornado args
args = sys.argv
args.append("--log_file_prefix=my_app.log")
if '--prod' in args:
    args.remove('--prod')

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