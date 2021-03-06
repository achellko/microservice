try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import os

class Scraper:
    folder= 'images/'

    def __init__(self):

        self.visited = set()
        self.session = requests.Session()
        self.session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}

        requests.packages.urllib3.disable_warnings()  # turn off SSL warnings

    def get_img(self, url):
        img_dict={}
        # if url in self.visited:
        #     return

        print('Starting to download images...')
        self.visited.add(url)
        content = self.session.get(url, verify=False).content
        soup = BeautifulSoup(content, "lxml")

        for img in soup.select("img[src]"):
            image_url = img["src"]
            if not image_url.startswith(("data:image", "javascript")):
                dict = self.download_img(urljoin(url, image_url))
            img_dict[dict[0]] = dict[1]
        return img_dict

    def download_img(self, image_url):
        img_name = image_url.split('/')[-1].split("?")[0]
        local_filename = self.folder + img_name

        r = self.session.get(image_url, stream=True, verify=False)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
        return [img_name,local_filename]

    def delete_img(self, file):
        if os.path.exists(file):
            os.remove(file)
        else:
            print("File {} does not exist".format(file))

    def check_fs_img(self, data={}):
        for file in os.listdir(self.folder):
            if not file in data.keys():
                data[file] = self.folder + file
        return data

    def update_img(self, data={}):
        for key in list(data):
            if not os.path.exists(self.folder + key) and not '.txt' in key:
                del data[key]
        return data