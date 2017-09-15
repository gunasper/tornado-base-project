import tornado.ioloop
import tornado.web
import sys
from tornado.log import enable_pretty_logging

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    settings = dict(
        debug=True
    )

    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)

if __name__ == "__main__":
    enable_pretty_logging()
    args = sys.argv
    args.append("--log_file_prefix=my_app.log")
    tornado.options.parse_command_line(args)

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
