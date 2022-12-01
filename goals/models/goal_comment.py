from django.contrib.auth import get_user_model
from django.db import models

from .base import DatesModelMixin
from .goal import Goal

USER_MODEL = get_user_model()


class GoalComment(DatesModelMixin):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"

    goal = models.ForeignKey(Goal, verbose_name="Цель", on_delete=models.CASCADE)
    user = models.ForeignKey(USER_MODEL, verbose_name='Автор', on_delete=models.CASCADE)
    text_comment = models.TextField(verbose_name="Текст")
