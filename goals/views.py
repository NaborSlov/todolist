from rest_framework import pagination, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from goals import serializers, models


class CreateGoalCatView(CreateAPIView):
    model = models.GoalCategory
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CreateGoalCatSerializer


class GoalCategoryListView(ListAPIView):
    model = models.GoalCategory
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
    model = models.GoalCategory
    serializer_class = serializers.GoalCategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance
