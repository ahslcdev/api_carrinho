from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.autenticacao.serializers import CreateUserSerializer, ListUserSerializer


@extend_schema_view(
    retrieve=extend_schema(description='text'),
    create=extend_schema(description='text'),
    list=extend_schema(description='text'),
    partial_update=extend_schema(description='text')
)
class UsuarioViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     GenericViewSet):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateUserSerializer
        return super().get_serializer_class()