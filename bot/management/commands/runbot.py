import os

from django.core.management import BaseCommand

from bot.tg.client import TgClient


class Command(BaseCommand):
    help = "Get message from tg bot"

    def get_message_from_tg_bot(self):
        offset = 0
        tg_client = TgClient(os.environ.get('TG_TOKEN'))
        while True:
            res = tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1

    def handle(self, *args, **options):
        self.get_message_from_tg_bot()
