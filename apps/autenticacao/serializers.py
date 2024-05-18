from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class CreateUserSerializer(ModelSerializer):
    """
    Serializer utilizado para se criar e atualizar dados de um usuário
    """
    class Meta:
        fields = [
            "password",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
        ]
        model = User

    def validate_password(self, data):
        data = make_password(data)
        return data
    

class ListUserSerializer(ModelSerializer):
    """
    Serializer utilizado para listagem geral e específica de usuários
    """
    class Meta:
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
        ]
        model = User