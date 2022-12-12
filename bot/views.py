from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from bot.models import TgUser
from bot.serializers import TgUserVerCodSerializer


class TgUserUpdate(generics.UpdateAPIView):
    model = TgUser
    serializer_class = (TgUserVerCodSerializer,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.model.objects.get(verification_code=self.request.data.get('verification_code'))
