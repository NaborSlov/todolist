from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username=None, password=None, **extra_fields):
        if not username:
            raise ValueError("У пользователя должен быть username")

        user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username=None, password=None, **extra_fields):
        if not username:
            raise ValueError("У суперпользователя должен быть username")

        if not password:
            raise ValueError("У суперпользователя должен быть пароль")

        user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

