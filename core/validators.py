from rest_framework.exceptions import ValidationError


def min_length_one(data):
    if len(data) < 1:
        return ValidationError("Поле не должен быть пустым")
