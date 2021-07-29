from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop


class IndexHandler(RequestHandler):
    def get(self):
        self.write("Hello, World!")



if __name__ == "__main__":
    app = Application(
        [
            (r"/", IndexHandler),
        ],
        debug=True,
    )

    app.listen(8001)
    instance = IOLoop.instance()
    instance.start()

