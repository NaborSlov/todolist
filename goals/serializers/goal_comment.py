from rest_framework.exceptions import ValidationError

from core.serializers import UserRetrieveUpdateSerializer
from goals import models
from goals.models import GoalComment
from goals.serializers import *


class CreateGoalCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalComment
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")

    def validate(self, attrs):
        role_use = models.BoardParticipant.objects.filter(
            user=attrs.get('user'),
            board=attrs.get('goal').category.board,
            role__in=[models.BoardParticipant.Role.owner, models.BoardParticipant.Role.writer]
        )

        if not role_use:
            raise ValidationError("Недостаточно прав")

        return attrs


class GoalCommentSerializer(serializers.ModelSerializer):
    user = UserRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = GoalComment
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user", "goal")
