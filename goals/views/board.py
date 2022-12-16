from django.db import transaction
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView

from goals import models, serializers
from goals.permissions import BoardPermission


class BoardCreateView(CreateAPIView):
    model = models.Board
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.BoardCreateSerializer


class BoardListView(ListAPIView):
    model = models.Board
    permission_classes = [BoardPermission]
    serializer_class = serializers.BoardListSerializer

    def get_queryset(self):
        return self.model.objects.filter(participants__user=self.request.user, is_deleted=False)


class BoardView(RetrieveUpdateDestroyAPIView):
    moder = models.Board
    permission_classes = [BoardPermission]
    serializer_class = serializers.BoardSerializer

    def get_queryset(self):
        return self.moder.objects.filter(participants__user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        """
        При удалении доски ее поле is_deleted меняется на True и у всех категорий этой
        доски поле is_deleted меняется тоже на True.
        У всех связанных целей поле status меняется на "В архиве"
        """
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.categories.update(is_deleted=True)
            models.Goal.objects.filter(category__board=instance).update(status=models.Goal.Status.archived)

        return instance
