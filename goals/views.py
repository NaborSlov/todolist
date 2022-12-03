from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from goals import models
from goals import serializers
from goals.filters import GoalDateFilter
from goals.models.goal import Status


class CreateGoalCatView(CreateAPIView):
    model = models.GoalCategory
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CreateGoalCatSerializer


class GoalCategoryListView(ListAPIView):
    model = models.GoalCategory
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.GoalCategorySerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    ordering_fields = ("title", "created",)
    search_fields = ("title",)

    def get_queryset(self):
        return self.model.objects.filter(
            user=self.request.user, is_deleted=False
        )


class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    model = models.GoalCategory
    serializer_class = serializers.GoalCategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True

        for goal in instance.goals.all():
            goal.status = Status.archived
            goal.save()

        instance.save()
        return instance


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


class GoalCommentCreateView(CreateAPIView):
    model = models.GoalComment
    serializer_class = serializers.CreateGoalCommentSerializer
    permission_classes = (IsAuthenticated,)


class GoalCommentListView(ListAPIView):
    model = models.GoalComment
    serializer_class = serializers.GoalCommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = (
        filters.OrderingFilter,
        DjangoFilterBackend
    )
    filterset_fields = ("goal",)
    ordering = ('-id',)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class GoalCommentView(RetrieveUpdateDestroyAPIView):
    model = models.GoalComment
    serializer_class = serializers.GoalCommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
