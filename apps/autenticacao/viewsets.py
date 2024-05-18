from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from apps.autenticacao.serializers import CreateUserSerializer, ListUserSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateUserSerializer
        return super().get_serializer_class()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            return queryset.filter(id=self.request.id)
        return queryset