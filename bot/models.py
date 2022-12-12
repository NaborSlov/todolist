from django.db import models


class TgUser(models.Model):
    chat_id = models.SmallIntegerField(verbose_name="id чата")
    user_ud = models.CharField(max_length=255, verbose_name="пользовательский идентификатор")
    user = models.ForeignKey("core.User", on_delete=models.PROTECT, null=True, blank=True, verbose_name="Пользователь")
