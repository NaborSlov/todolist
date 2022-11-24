import json

from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import User
from core.serializers import UserRegistrationSerializer, UserLoginSerializer, UserRetrieveUpdateSerializer, \
    UserChangePasswordSerializer


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            if serializer.data.get('password') != serializer.data.get('password_repeat'):
                return Response({"password_repeat": ["Пароли не совпадают"]}, status=status.HTTP_400_BAD_REQUEST)

            obj = serializer.data
            del obj['password_repeat']
            obj['password'] = make_password(obj.get('password'))
            self.queryset.create(**obj)
            response = {
                'status': 'success',
                'code': status.HTTP_201_CREATED,
                'message': 'Пользователь создан',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class UserLoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(UserLoginSerializer(user).data)

        return JsonResponse({'error': 'Invalid login'}, status=404)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = get_user(self.request)
        return user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=204)


class PasswordUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_user(self.request)
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=self.request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Неправильный пароль"]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Пароль обновлен',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
