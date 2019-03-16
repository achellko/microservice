from flask import Flask
from flask_restful import Resource, Api
import txt
import img

app = Flask(__name__)
api = Api(app)

data = {}
text = txt.Text()
scraper = img.Scraper()

"""
Update data-json so it will represent an
actual content of 'images' and 'text' folders
"""
data.update(text.check_fs_text(data))
data.update(scraper.check_fs_img(data))

"""
RESTful API with CRUD functions
"""
class Data(Resource):

    """
    READ: shows current version of data-json
    """
    def get(self, content_type, url):
        print("Running PUT")
        global data
        return data

    """
    CREATE: this function uploads content from given url: 
    depending on 'content_type' flag, it will upload
    all images from given webpage, or its text content
    """
    def post(self, content_type, url):
        global data
        print("Running POST")
        if content_type.lower() == "text":
            dict = text.get_text(url)
            data.update(dict)

        elif content_type.lower() == "image":
            dict = scraper.get_img(url)
            data.update(dict)
        else:
            return "Wrong type, must be 'text' or 'image'", 400

        return data, 201

    """
    DELETE: deletes file from file system and data-json
    """
    def delete(self, content_type, url):
        global data
        print("Running DELETE")
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

    """
    UPDATE: updates data-json, if some files don`t exist in file system,
    it deletes them from data-json
    """
    def put(self, content_type, url):
        global data
        print("Running PUT")
        if content_type.lower() == 'text':
            data = text.update_text(data)
        elif content_type.lower() == 'image':
            data = scraper.update_img(data)
        else:
            return "Wrong type, must be 'text' or 'image'", 400

        return data, 200

api.add_resource(Data, "/api/<string:content_type>/<path:url>")
app.run(debug=True)
