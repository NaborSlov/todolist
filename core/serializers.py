from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from core.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password", 'password_repeat')

    def validate_password(self, data):
        validate_password(data)

        return data


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate_new_password(self, data):
        validate_password(data)
        return data
