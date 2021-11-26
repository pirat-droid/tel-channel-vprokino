from create_db import CreateDB
from network import Internet
from parsing import Parsing
from datetime import datetime
from telegram import Telegram
import httplib2


def create_message():
    db = CreateDB('message.sqlite3')
    db.create_connect()

    if not Internet('https://ya.ru/').check():
        print('Internet connect Lost!')
        exit()

    news = Parsing('https://www.kinomania.ru/news')
    message1 = news.get_data('div', 'pagelist-item-title')
    message2 = news.get_find_next('div', 'pagelist-item-title', 'p')
    a = news.get_data('div', 'pagelist-item', True)

    h = httplib2.Http('.cache')
    response, content = h.request('http:' + a[0])
    out = open(f'./image/{datetime.today().strftime("%Y-%m-%d-%H:%M:%S")}.jpg', 'wb')
    out.write(content)
    out.close()

    mes = Telegram('VPROkino', message1[0] + '\n' + message2[0], f'./image/{datetime.today().strftime("%Y-%m-%d-%H:%M:%S")}.jpg')
    mes.send_message()


if __name__ == '__main__':
    create_message()
