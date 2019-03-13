from flask import Flask
from flask_restful import Resource, Api
import txt
import img
import json

app = Flask(__name__)
api = Api(app)

data = [
    { }
]

class Data(Resource):
    def get(self, url):
        for link in data:
            if(url == link['url']):
                return url, 200
        return "Not found", 404

    def post(self, type, url):
        if type.lower() == "text":
            text = txt.Text()
            dict = text.get_text(url)
            data = json.dumps(dict)
            print(data)

        elif type.lower() == "image":
            scraper = img.Scraper()
            dict = scraper.get_img(url)
            data = json.dumps(dict)

        print(data)
        return data[url], 200

    def put(self, url):
        return

    def delete(self, url):
        return

# print(str(txt.Text().get_text('https://gist.github.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a')))
# print(str(img.Scraper().get_img('https://gist.github.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a')))

api.add_resource(Data, "/api/<string:type>/<string:url>")

app.run(debug=True)
