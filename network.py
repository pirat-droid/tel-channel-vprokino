import requests as requests


class Internet:

    def __init__(self, address):
        self.address = address

    def check(self):
        try:
            requests.get(self.address)
            print('Internet connect Yes')
            return True
        except:
            return False
