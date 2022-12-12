from rest_framework import serializers

from bot.models import TgUser


class TgUserVerCodSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    verification_code = serializers.CharField(max_length=255)

    class Meta:
        model = TgUser
        fields = "__all__"
        read_only_fields = ("id", "chat_id", "user_ud")

    def update(self, instance, validated_data):
        instance.update(user=validated_data.get('user'))
        return instance
