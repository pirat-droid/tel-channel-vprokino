from create_db import CreateDB
from network import Internet
from parsing import Parsing


def create_message():
    db = CreateDB('message.sqlite3')
    db.create_connect()

    if not Internet('https://ya.ru/').check():
        print('Internet connect Lost!')
        exit()

    premieres_today = Parsing('https://www.kinoafisha.info/movies/')
    title_t = premieres_today.get_data('span', 'movieItem_title')
    subtitle_t = premieres_today.get_data('span', 'movieItem_subtitle')
    genres_t = premieres_today.get_data('span', 'movieItem_genres')
    country_t = premieres_today.get_data('span', 'movieItem_year')

    i = 0
    move = []
    while i < len(title_t):
        dict = {'title': title_t[i], 'subtitle': subtitle_t[i], 'genres': genres_t[i], 'country': country_t[i]}
        move.append(dict)
        i += 1
    print(move)

if __name__ == '__main__':
    create_message()
# create message




























# premieres_month = Parsing('https://www.kinoafisha.info/releases/2021/11/')
# title_m = premieres_month.get_data('span', 'movieItem_title')
# subtitle_m = premieres_month.get_data('span', 'movieItem_subtitle')
# genres_m = premieres_month.get_data('span', 'movieItem_genres')
# country_m = premieres_month.get_data('span', 'movieItem_year')
#
# print(title_m)
# print(subtitle_m)
# print(genres_m)
# print(country_m)
#
# # убрать спец символы
# news = Parsing('https://www.kinomania.ru/news')
# p = news.get_data('div', 'news-pagelist-item-content')
# print(p)
# a = news.get_data('div', 'pagelist-item', True)
# print(a)
