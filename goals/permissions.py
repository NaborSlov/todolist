from rest_framework import permissions
from django.db.models import Q

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


class CategoryPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return models.GoalCategory.objects.filter(board__participants__user=request.user).exists()

        role_search = (Q(board__participants__role=models.BoardParticipant.Role.owner) |
                       Q(board__participants__role=models.BoardParticipant.Role.writer))

        return models.GoalCategory.objects.filter(
            role_search,
            board__participants__user=request.user,
            id=obj.id,
        ).exists()
