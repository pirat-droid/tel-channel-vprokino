from telethon import TelegramClient, sync, events
from authentication import *


class Telegram:
    def __init__(self, channel, message, image=None):
        self.channel = channel
        self.message = message
        self.client = TelegramClient(phone, api_id, api_hash).start()
        self.image = image

    def send_message(self):
        if self.image is not None:
            self.client.send_file(self.channel, self.image, caption=self.message)
        else:
            self.client.send_message(self.channel, self.message)
