from flask import Flask
from flask_restful import Resource, Api
import txt
import img
import json

app = Flask(__name__)
api = Api(app)

data = [
    {
        '97bfd34132394e23ca5905ec730f776a': 'text/97bfd34132394e23ca5905ec730f776a.txt'
    }
]

class Data(Resource):
    def get(self, type, url):
        print("GET")
        for link in data:
            if(url == link['url']):
                return url, 200
            else:
                return "Not found", 404

    def post(self, type, url):
        print("POST")
        if type.lower() == "text":
            text = txt.Text()
            dict = text.get_text(url)
            #data.append(json.dumps(dict))
            data = json.dumps(dict)

        elif type.lower() == "image":
            scraper = img.Scraper()
            dict = scraper.get_img(url)
            data = json.dumps(dict)
            #data.append(json.dumps(dict))

        print(str(data))
        return data, 200

    def put(self, url):
        return

    def delete(self, url):
        return

api.add_resource(Data, "/api/<string:type>/<path:url>")

app.run(debug=True)
