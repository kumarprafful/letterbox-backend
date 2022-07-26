from django.contrib.auth import authenticate, login, logout
from letterbox.exceptions import LBException
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.serializers import UserLiteSerializer, UserRegisterSerializer


class AuthViewset(viewsets.GenericViewSet):

    @action(detail=False, methods=['POST'], url_path='register', permission_classes=[AllowAny])
    def register(self, request):
        data = request.data
        serializer = UserRegisterSerializer(
            data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if user.is_active is False:
            return Response({'message': 'user is not active'}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'token': token.key}, status=200)

    @action(detail=False, methods=['POST'], url_path='login', permission_classes=[AllowAny])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        token = request.data.get('token')

        if not ((email and password) or token):
            return Response({'message': 'credentials not provided'}, status=400)
        try:
            user = authenticate(
                request=request, username=email, password=password)
            if user is None:
                raise LBException('invalid credentials')
        except LBException as e:
            return Response({'message': str(e)}, status=400)

        if user.is_active is False:
            return Response({'message': 'user is not active'}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'token': token.key}, status=200)

    @action(detail=False, methods=['get'], url_path='logout', permission_classes=[IsAuthenticated])
    def logout(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            logout(request)
        return Response(status=200)

    @action(detail=False, methods=['get'], url_path='me', permission_classes=[IsAuthenticated])
    def about_me(self, request):
        user = request.user
        serializer = UserLiteSerializer(user)
        return Response(serializer.data, status=200)

    