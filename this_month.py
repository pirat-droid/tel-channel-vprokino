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

    premieres_today = Parsing('https://www.kinoafisha.info/movies/')
    title = premieres_today.get_data('span', 'movieItem_title')
    subtitle = premieres_today.get_data('span', 'movieItem_subtitle')
    genres = premieres_today.get_data('span', 'movieItem_genres')
    country = premieres_today.get_data('span', 'movieItem_year')

    check_month = {'1': 'ЯНВАРЯ',
                   '2': 'ФЕВРАЛЯ',
                   '3': 'МАРТА',
                   '4': 'АПРЕЛЯ',
                   '5': 'МАЯ',
                   '6': 'ИЮНЯ',
                   '7': 'ИЮЛЯ',
                   '8': 'АВГУСТА',
                   '9': 'СЕНТЯБРЯ',
                   '10': 'ОКТЯБРЯ',
                   '11': 'НОЯБРЯ',
                   '12': 'ДЕКАБРЯ'}

    i = 0
    message = '\n\nКИНО ПРЕМЬЕРЫ ' + check_month[str(datetime.now().month)] + ' 🎥 \n\n'
    while i < len(title):
        message += f'🎞 {title[i]} - {subtitle[i]}'
        message += '\n' + f'жанр: {genres[i]}.' + '\n' + f'Cтрана {country[i].replace(str(datetime.now().year) + ",", "")}' + '\n\n'
        i += 1

    print(message)
    mes = Telegram('VPROkino', message)
    mes.send_message()


if __name__ == '__main__':
    create_message()

# # убрать спец символы
# news = Parsing('https://www.kinomania.ru/news')
# p = news.get_data('div', 'news-pagelist-item-content')
# print(p)
# a = news.get_data('div', 'pagelist-item', True)
# print(a)
