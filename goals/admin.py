from django.contrib import admin

from goals import models


@admin.register(models.GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "create", "update")
    search_fields = ("title", "user__username")
