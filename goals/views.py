from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from goals import serializers
from goals.filters import GoalDateFilter
from goals.models.goal import Goal
from goals.models.goal_category import GoalCategory
from goals.models.goal_comment import GoalComment


class CreateGoalCatView(CreateAPIView):
    model = GoalCategory
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CreateGoalCatSerializer


class GoalCategoryListView(ListAPIView):
    model = GoalCategory
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.GoalCategorySerializer
    pagination_class = pagination.LimitOffsetPagination
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
    model = GoalCategory
    serializer_class = serializers.GoalCategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance


class GoalCreateView(CreateAPIView):
    model = Goal
    serializer_class = serializers.CreateGoalSerializer
    permission_classes = (IsAuthenticated,)


class GoalListView(ListAPIView):
    model = Goal
    serializer_class = serializers.GoalSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = GoalDateFilter

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class GoalView(RetrieveUpdateDestroyAPIView):
    model = Goal
    serializer_class = serializers.GoalSerializer
    permission_classes = (IsAuthenticated,)


class GoalCommentCreateView(CreateAPIView):
    model = GoalComment
    serializer_class = serializers.CreateGoalCommentSerializer
    permission_classes = (IsAuthenticated,)


class GoalCommentListView(ListAPIView):
    model = GoalComment
    serializer_class = serializers.GoalCommentSerializer
    permission_classes = (IsAuthenticated,)


class GoalCommentView(RetrieveUpdateDestroyAPIView):
    model = GoalComment
    serializer_class = serializers.GoalCommentSerializer
    permission_classes = (IsAuthenticated,)
