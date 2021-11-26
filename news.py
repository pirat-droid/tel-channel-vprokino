from create_db import CreateDB
from network import Internet
from parsing import Parsing
from datetime import datetime
from telegram import Telegram


def create_message():
    db = CreateDB('message.sqlite3')
    db.create_connect()

    if not Internet('https://ya.ru/').check():
        print('Internet connect Lost!')
        exit()

    # убрать спец символы
    news = Parsing('https://www.kinomania.ru/news')
    message = news.get_data('div', 'news-pagelist-item-content')
    a = news.get_data('div', 'pagelist-item', True)
    # print(a)

    print(message[2])
    # mes = Telegram('VPROkino', message)
    # mes.send_message()


if __name__ == '__main__':
    create_message()

#

