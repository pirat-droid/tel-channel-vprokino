from bs4 import BeautifulSoup


class ParsingPost:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
