import json
import os
import tornado.ioloop
import tornado.web

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    }

cereals = json.load(open("static/data/cereals.json"))
cereal_names = set(cereals.keys())

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/index.html")

class CerealHandler(tornado.web.RequestHandler):

    def get(self, cereal_id=None):
        print cereal_id
        if not cereal_id:
            cereal = False
        elif cereal_id in cereal_names:
            cereal = cereals[cereal_id]
        else:
            raise tornado.web.HTTPError(404)
        self.render("templates/cereals.html", cereal=cereal)


class AboutHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/about.html")


class DownloadHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/download.html")


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/cereals/(\w+)", CerealHandler),
    (r"/cereals", CerealHandler),
    (r"/about", AboutHandler),
    (r"/export", DownloadHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
