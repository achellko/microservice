import io
import os
import html2text
import requests as reqs

class Text:
    folder = 'text/'

    def get_text(self, url):
        txt_dict={}
        response = reqs.get(url)

        txt_name = (url.split('/')[-1].split("?")[0] if url.split('/')[-1] else url.split('http')[1].split('/')[-2])
        local_filename = self.folder + txt_name

        with io.open(local_filename, "w", encoding="utf-8") as file:
            file.write(html2text.html2text(response.text))
            file.close()
            txt_dict[txt_name] = local_filename
        return txt_dict

    def delete_text(self, file):
        if os.path.exists(file):
            os.remove(file)
        else:
            print("File {} does not exist".format(file))

    def check_fs_text(self, data={}):
        for file in os.listdir(self.folder):
            if not file in data.keys():
                data[file] = self.folder + file
        return data

    def update_text(self, data={}):
        for key in list(data):
            if not os.path.exists(self.folder + key) and '.txt' in key:
                del data[key]
        return data
