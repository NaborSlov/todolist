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
            return models.BoardParticipant.objects.filter(user=request.user, board=obj.board).exists()

        return models.BoardParticipant.objects.filter(
            user=request.user,
            board=obj.board,
            role__in=[models.BoardParticipant.Role.owner, models.BoardParticipant.Role.writer]
        ).exists()


class GoalPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return models.BoardParticipant.objects.filter(user=request.user, board=obj.category.board).exists()

        return models.BoardParticipant.objects.filter(
            user=request.user,
            board=obj.category.board,
            role__in=[models.BoardParticipant.Role.owner, models.BoardParticipant.Role.writer]
        ).exists()


class GoalCommentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return models.BoardParticipant.objects.filter(user=request.user, board=obj.goal.category.board).exists()

        return models.BoardParticipant.objects.filter(
            user=request.user,
            board=obj.goal.category.board,
            role__in=[models.BoardParticipant.Role.owner, models.BoardParticipant.Role.writer]
        ).exists()
