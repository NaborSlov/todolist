from rest_framework import permissions

from goals import models


class BoardPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return models.BoardParticipant.objects.filter(user=request.user).exists()

        return models.BoardParticipant.objects.filter(
            user=request.user,
            board=obj,
            role=models.BoardParticipant.Role.owner
        ).exists()
