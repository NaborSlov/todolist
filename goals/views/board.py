from django.db import transaction
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from goals import models, serializers
from goals.permissions import BoardPermission


class BoardView(RetrieveUpdateDestroyAPIView):
    moder = models.Board
    permission_classes = [BoardPermission]
    serializer_class = serializers.BoardSerializer

    def get_queryset(self):
        return self.moder.objects.filter(participants__user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.categories.update(is_deleted=True)
            models.Goal.objects.filter(category__board=instance).update(status=models.Goal.Status.archived)
