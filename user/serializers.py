from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'image', 'role', 'is_blocked')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'image')
        extra_kwargs = {
            'password': {'write_only': True,
                         'required': True,
                         'validators': [validate_password]
                         }
        }

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
