import requests
from bs4 import BeautifulSoup


class Parsing:

    def __init__(self, link):
        try:
            req = requests.get(link)
        except:
            print('Can not open link %s' % link)
            exit()
        self.soup = BeautifulSoup(req.text, 'html.parser')

    def get_data(self, tag, class_name, img=False):
        elements = self.soup.find_all(tag, class_name)
        data = []
        for element in elements:
            if img:
                # print(element)
                data.append(element.img['data-original'])
            else:
                data.append(element.get_text())
        return data
