import os
import tornado.ioloop
import tornado.web

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
}

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/index.html")

class CerealHandler(tornado.web.RequestHandler):

    def get(self, cereal_id=None):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/cereals", CerealHandler),
    (r"/cereals/[\w]+", CerealHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
