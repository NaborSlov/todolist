from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from goals import models, serializers
from goals.permissions import CategoryPermission


class CreateGoalCatView(CreateAPIView):
    model = models.GoalCategory
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CreateGoalCatSerializer


class GoalCategoryListView(ListAPIView):
    model = models.GoalCategory
    permission_classes = (CategoryPermission,)
    serializer_class = serializers.GoalCategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    filterset_fields = ('board',)
    ordering_fields = ("title", "created",)
    search_fields = ("title",)

    def get_queryset(self):
        return self.model.objects.filter(is_deleted=False, board__participants__user=self.request.user)


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    model = models.GoalCategory
    serializer_class = serializers.GoalCategorySerializer
    permission_classes = (CategoryPermission,)

    def get_queryset(self):
        return self.model.objects.filter(is_deleted=False, board__participants__user=self.request.user)

    def perform_destroy(self, instance):
        with transaction.atomic():
            instance.is_deleted = True
            instance.save()
            instance.goals.update(status=models.Goal.Status.archived)

        return instance
