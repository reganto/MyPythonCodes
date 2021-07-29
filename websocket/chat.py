# Author: Reganto
# Blog: reganto.net
# Modified Tornado: github.com/reganto/tornado

from tornado import web, websocket, ioloop


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('chat.html')


class ChatConnection(websocket.WebSocketHandler):
    participants = set()

    def on_open(self):
        self.broadcast(self.participants, 'Someone joined.')
        self.participants.add(self)

    def on_message(self, message):
        self.broadcast(self.participants, message)

    def on_close(self):
        self.participants.remove(self)
        self.broadcast(self.participants, 'Someone left.')


if __name__ == "__main__":
    app = web.Application([
        ('/', IndexHandler),
        ('/chat', ChatConnection)
    ], debug=True)
    app.listen(8081)
    ioloop.IOLoop.current().start()
