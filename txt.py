import io
import os
import html2text
import requests as reqs

class Text:
    def get_text(self, url):
        txt_dict={}
        response = reqs.get(url)

        txt_name = url.split('/')[-1].split("?")[0]+'.txt'
        local_filename = 'text/'+txt_name

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


