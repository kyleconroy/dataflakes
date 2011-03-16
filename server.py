import json
import os
import tornado.ioloop
import tornado.web
import stats

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    }

cereals = json.load(open("static/data/cereals.json"))
cereal_list = sorted([ cereals[k] for k in cereals.iterkeys() ],
                     key=lambda x: x["name"])
cereal_names = set(cereals.keys())
pie_charts = json.load(open("static/data/piecharts.json"))

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        scatter = open("static/data/names.json")
        shelf = open("static/data/shelf.json")
        data = [ {"name": v["name"], "x": int(v["sugars"])}
                 for v in cereals.itervalues() ]
        self.render("templates/index.html", shelfs=shelf.read(),
                    scatter=scatter.read(),
                    bran=json.dumps(pie_charts["bran-chex"]),
                    bran_name="Bran Chex")


class CerealInstanceHandler(tornado.web.RequestHandler):

    def get(self, cereal_id=None):
        if cereal_id in cereal_names:
            cereal = cereals[cereal_id]
            self.render("templates/cereals.html", cereal=cereal,
                        data=stats.rdi(cereal))
        else:
            raise tornado.web.HTTPError(404)


class CerealListHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/cereals.html", cereal=False,
                    cereals=cereal_list)


class CerealListResource(tornado.web.RequestHandler):

    def get(self):
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps({"cereals": cereals}))


class CerealInstanceResource(tornado.web.RequestHandler):

    def get(self, cereal_id=None):
        if cereal_id in cereal_names:
            cereal = cereals[cereal_id]
        else:
            raise tornado.web.HTTPError(404)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(cereal))


class ComparisonHandler(tornado.web.RequestHandler):

    def get(self):
        data = [ c for c in cereals.itervalues() ]
        self.render("templates/comparison.html", data=json.dumps(data))


class AboutHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/about.html")


class DownloadHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/download.html")


application = tornado.web.Application([

    # Normal
    (r"/", MainHandler),
    (r"/cereals/([\w-]+)", CerealInstanceHandler),
    (r"/cereals", CerealListHandler),
    (r"/about", AboutHandler),
    (r"/export", DownloadHandler),
    (r"/comparison", ComparisonHandler),

    # API
    (r"/api/cereals/([\w-]+)", CerealInstanceResource),
    (r"/api/cereals", CerealListResource),

], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
