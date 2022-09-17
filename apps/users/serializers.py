from rest_framework import serializers
from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer
)

class UserCreateSerializer(BaseUserCreateSerializer):
    
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 
                   'email', 'first_name', 'last_name']
    
class CustomUserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):

        fields = ['id', 'username', 'email', 'first_name', 'last_name']
