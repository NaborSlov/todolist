from django.db import models

from goals.models.base import DatesModelMixin


class Board(DatesModelMixin):
    class Meta:
        verbose_name = "Доска"
        verbose_name_plural = "Доски"

    title = models.CharField(max_length=255, verbose_name="Название доски")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалена")


class BoardParticipant(DatesModelMixin):
    class Meta:
        verbose_name = "Участник доски"
        verbose_name_plural = "Участники доски"
        unique_together = ("user", "board")


    class Role(models.IntegerChoices):
        owner = 1, "Владелец"
        writer = 2, "Редактор"
        reader = 3, "Читатель"

    user = models.ForeignKey("core.User", verbose_name='Автор', on_delete=models.PROTECT, related_name="users")
    board = models.ForeignKey(Board, verbose_name="Доска", on_delete=models.PROTECT, related_name="many_board")
    role = models.PositiveSmallIntegerField(verbose_name="Роль", choices=Role.choices, default=Role.owner)
