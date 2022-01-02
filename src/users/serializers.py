from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password as vp
from users.models import User


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField()
    source = serializers.CharField(required=False)
    password = serializers.CharField()

    def get_cleaned_data(self):
        return {
            'password': self.validated_data['password'],
            'email': self.validated_data['email'],
            'phone': self.validated_data['phone'],
            'source': self.validated_data.get('source'),
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'User with this email already exits')
        return value

    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError(
                'User with this phone already exits')
        return value

    def validate_password(self, value):
        vp(value)
        return

    def create(self, validated_data):
        user = User.objects.create(
            phone=validated_data['phone'],
            email=validated_data['email'],
            source=validated_data.get('source')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TokenUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', ]
