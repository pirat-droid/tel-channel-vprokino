from telethon import TelegramClient, sync, events
from authentication import *


class Telegram:
    def __init__(self, channel, message):
        self.channel = channel
        self.message = message
        self.client = TelegramClient(phone, api_id, api_hash).start()

    def send_message(self):
         self.client.send_message(self.channel, self.message)
