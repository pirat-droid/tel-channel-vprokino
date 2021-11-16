from create_db import CreateDB
from network import Internet

db = CreateDB('message.sqlite3')
db.create_connect()

if not Internet('https://ya.ru/').check():
    print('Internet connect Lost!')

# parsing site
# https://www.kinoafisha.info/movies/ в прокате сейчас, брать раз в три дня, парсинг
# https://www.kinopoisk.ru/premiere/ru/2021/month/11/ премьеры каждый день, парсинг


