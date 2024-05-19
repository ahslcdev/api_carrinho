from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.core.api.filters import PedidoFilters
from apps.core.models import Item, Pedido
from apps.core.api.serializers import CreatePedidoSerializer, ItemSerializer, ListPedidoSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ['post', 'get', 'patch', 'delete', ]


class PedidoViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Pedido.objects.all()
    serializer_class = ListPedidoSerializer
    filterset_class = PedidoFilters

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action == 'create':
            serializer = CreatePedidoSerializer
        return serializer