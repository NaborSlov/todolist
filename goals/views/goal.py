from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from goals import models, serializers
from goals.filters import GoalDateFilter
from goals.models.goal import Status


class GoalCreateView(CreateAPIView):
    model = models.Goal
    serializer_class = serializers.CreateGoalSerializer
    permission_classes = (IsAuthenticated,)


class GoalListView(ListAPIView):
    model = models.Goal
    serializer_class = serializers.GoalSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = GoalDateFilter
    ordering_fields = ("title", "id",)
    search_fields = ("title",)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class GoalView(RetrieveUpdateDestroyAPIView):
    model = models.Goal
    serializer_class = serializers.GoalSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        instance.status = Status.archived
        instance.save()
        return instance


