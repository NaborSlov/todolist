from rest_framework.exceptions import ValidationError

from core.serializers import UserRetrieveUpdateSerializer
from goals import models
from goals.models import GoalCategory
from goals.serializers import *


class CreateGoalCatSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = "__all__"

    def validate(self, attrs):
        role_user = models.BoardParticipant.objects.filter(
            user=attrs.get('user'),
            board=attrs.get('board'),
            role__in=[models.BoardParticipant.Role.owner, models.BoardParticipant.Role.writer]
        ).exists()

        if not role_user:
            raise ValidationError("Недостаточно прав")

        return attrs


class GoalCategorySerializer(serializers.ModelSerializer):
    user = UserRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user", "board")
