import sys
import tornado.ioloop

from tornado.log import enable_pretty_logging
from routes import ROUTES
from application import Application

PORT = 8080

if __name__ == "__main__":
    enable_pretty_logging()
    args = sys.argv
    args.append("--log_file_prefix=my_app.log")
    tornado.options.parse_command_line(args)

    app = Application(ROUTES)
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
