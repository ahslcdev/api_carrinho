from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.autenticacao.serializers import CreateUserSerializer, ListUserSerializer


@extend_schema_view(
    retrieve=extend_schema(description='Listagem específica de usuários'),
    create=extend_schema(description='Criação de usuários'),
    list=extend_schema(description='Listagem geral de usuários'),
    partial_update=extend_schema(description='Update parcial de usuários'),
)
class UsuarioViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     GenericViewSet):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer

    def get_serializer_class(self):
        serializer_classe = super().get_serializer_class()
        if self.action in ['create', 'partial_update', 'put']:
            serializer_classe = CreateUserSerializer
        return serializer_classe