# Author: Reganto
# Blog: reganto.net
# Modified Tornado: github.com/reganto/tornado

from tornado.ioloop import PeriodicCallback, IOLoop
from tornado.web import RequestHandler, Application, url
from tornado.websocket import WebSocketHandler


class TickerConnection(WebSocketHandler):
    def on_open(self):
        self._timeout = PeriodicCallback(self._ticker, 1000)
        self._timeout.start()

    def on_close(self):
        self._timeout.close()
        
    def _ticker(self):
        self.send("tick!")


class IndexHandler(RequestHandler):
    def get(self):
        self.render("ticker.html")



if __name__ == "__main__":
    app = Application(
        [
            url("/", IndexHandler, name="index"),
            url("/ws", TickerConnection, name="ticker"),
        ],
        debug=True,
    )
    app.listen(8001)
    IOLoop.current().start()
 
