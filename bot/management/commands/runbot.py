import os

from django.core.management import BaseCommand

from bot.models import TgUser
from bot.tg.client import TgClient
from bot.utils import generator_code_verification


class Command(BaseCommand):
    help = "Get message from tg bot"

    def get_message_from_tg_bot(self):
        offset = 0
        tg_client = TgClient(os.environ.get('TG_TOKEN'))
        while True:
            res = tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                user_tg = TgUser.objects.get(user_ud=item.message.from_.id)
                ver_cod = generator_code_verification()

                if not user_tg:
                    TgUser.objects.create(user_ud=item.message.from_.id,
                                          chat_id=item.message.chat.id,
                                          verification_code=ver_cod)

                    tg_client.send_message(
                        chat_id=item.message.chat.id,
                        text=f"Привет новый пользователь\n"
                             f"Код верификации - {ver_cod}"
                    )

                if not user_tg.user:
                    user_tg.verification_code = ver_cod
                    user_tg.save()
                    tg_client.send_message(
                        chat_id=item.message.chat.id,
                        text=f"Подтвердите свой аккаунт\n"
                             f"Код верификации - {ver_cod}")

    def handle(self, *args, **options):
        self.get_message_from_tg_bot()
