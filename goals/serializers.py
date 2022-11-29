from rest_framework import serializers

from core.serializers import UserRetrieveUpdateSerializer
from goals import models


class CreateGoalCatSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.GoalCategory
        read_only_fields = ('id', 'create', 'update', 'user')
        fields = "__all__"


class GoalCategorySerializer(serializers.ModelSerializer):
    user = UserRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = models.GoalCategory
        fields = "__all__"
        read_only_fields = ("id", "create", "update", "user")
