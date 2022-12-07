from rest_framework.exceptions import ValidationError

from core.serializers import UserRetrieveUpdateSerializer
from goals import models
from goals.models import Goal
from goals.serializers import *


class CreateGoalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")

    def validate(self, attrs):
        role_use = models.BoardParticipant.objects.filter(
            user=attrs.get('user'),
            board=attrs.get('category').board,
            role__in=[models.BoardParticipant.Role.owner, models.BoardParticipant.Role.writer]
        )

        if not role_use:
            raise ValidationError("Недостаточно прав")

        return attrs


class GoalSerializer(serializers.ModelSerializer):
    user = UserRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("not allowed in deleted category")

        if value.user != self.context["request"].user:
            raise serializers.ValidationError("not owner of category")

        return value
