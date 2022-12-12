import math
import random
import string


def generator_code_verification():
    """
    Функция для генерации кода верификации
    """
    letters = string.digits + string.ascii_lowercase + string.ascii_uppercase
    ver_cod = ""
    for _ in range(25):
        ver_cod += letters[math.floor(random.random() * len(letters))]

    return ver_cod
