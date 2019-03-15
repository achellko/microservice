from flask import Flask
from flask_restful import Resource, Api
import txt
import img

app = Flask(__name__)
api = Api(app)

data = {}
text = txt.Text()
scraper = img.Scraper()

data.update(text.check_fs_text(data))
data.update(scraper.check_fs_img(data))

class Data(Resource):
    def get(self, content_type, url):
        global data
        return data

    def post(self, content_type, url):
        global data
        if content_type.lower() == "text":
            dict = text.get_text(url)
            data.update(dict)

        elif content_type.lower() == "image":
            dict = scraper.get_img(url)
            data.update(dict)
        else:
            return "Wrong type, must be 'text' or 'image'", 400

        return data, 201

    def delete(self, content_type, url):
        global data
        try:
            if content_type.lower() == 'text':
                text.delete_text(data[url])
                del data[url]
            elif content_type.lower() == 'image':
                scraper.delete_img(data[url])
                del data[url]
            else:
                return "Wrong type, must be 'text' or 'image'", 400

            return "File {} was deleted".format(url), 200
        except KeyError:
            return "No such element: {}".format(url), 400

    def put(self, content_type, url):
        global data
        if content_type.lower() == 'text':
            data = text.update_text(data)
        elif content_type.lower() == 'image':
            data = scraper.update_img(data)
        else:
            return "Wrong type, must be 'text' or 'image'", 400

        return data, 200
api.add_resource(Data, "/api/<string:content_type>/<path:url>")

app.run(debug=True)
