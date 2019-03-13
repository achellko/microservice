from flask import Flask
from flask_restful import Resource, Api
import txt
import img
import json

app = Flask(__name__)
api = Api(app)

data = {}

class Data(Resource):
    def get(self, content_type, url):
        global data
        return data, 200

    def post(self, content_type, url):
        global data
        if content_type.lower() == "text":
            text = txt.Text()
            dict = text.get_text(url)
            data.update(dict)

        elif content_type.lower() == "image":
            scraper = img.Scraper()
            dict = scraper.get_img(url)
            data.update(dict)

        return data, 201

    def delete(self, content_type, url):
        global data
        try:
            del data[url]
            return "File {} was deleted".format(url), 200
        except KeyError:
            return "No such element: {}".format(url), 400

api.add_resource(Data, "/api/<string:content_type>/<path:url>")

app.run(debug=True)
