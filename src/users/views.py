from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers import UserRegisterSerializer


class AuthViewset(viewsets.GenericViewSet):

    @action(detail=False, methods=['POST'], url_path='register', permission_classes=[AllowAny])
    def register(self, request):
        data = request.data
        serializer = UserRegisterSerializer(
            data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)
