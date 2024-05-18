from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class CreateUserSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User

    def validate_password(self, data):
        data = make_password(data)
        return data
    

class ListUserSerializer(ModelSerializer):
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