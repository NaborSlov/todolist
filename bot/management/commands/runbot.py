import os

from django.core.management import BaseCommand

from bot.models import TgUser
from bot.tg import tg_client
from bot.utils import generator_code_verification
from goals.models import Goal


class Command(BaseCommand):
    help = "Get message from tg bot"
    tg_client = tg_client

    def get_message_from_tg_bot(self):
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1

                user_tg = TgUser.objects.get(user_ud=item.message.from_.id)

                ver_cod = generator_code_verification()

                if not user_tg:
                    TgUser.objects.create(user_ud=item.message.from_.id,
                                          chat_id=item.message.chat.id,
                                          verification_code=ver_cod)

                    self.tg_client.send_message(
                        chat_id=item.message.chat.id,
                        text=f"Привет новый пользователь\n"
                             f"Код верификации - {ver_cod}"
                    )
                    continue

                if not user_tg.user:
                    user_tg.verification_code = ver_cod
                    user_tg.save()
                    self.tg_client.send_message(
                        chat_id=item.message.chat.id,
                        text=f"Подтвердите свой аккаунт\n"
                             f"Код верификации - {ver_cod}")
                    continue

                if item.message.text != "/goals":
                    self.tg_client.send_message(
                        chat_id=item.message.chat.id,
                        text="Неизвестная команда"
                    )
                    continue

                goals = (Goal.objects.filter(category__board__participants__user=user_tg.user).
                         exclude(status=Goal.Status.archived))

                if not goals:
                    self.tg_client.send_message(
                        chat_id=item.message.chat.id,
                        text=f"На сегодня ничего нет")

                for goal in goals:
                    self.tg_client.send_message(
                        chat_id=item.message.chat.id,
                        text=f"{goal.title}\n"
                             f"{goal.description}\n"
                             f"Категория - {goal.category}\n"
                             f"Приоритет - {goal.Priority.choices[goal.priority - 1][1]}\n"
                             f"Дедлайн - {goal.due_date}"
                    )

    def handle(self, *args, **options):
        self.get_message_from_tg_bot()
