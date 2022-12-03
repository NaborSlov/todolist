from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from goals import models, serializers


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
