from rest_framework.viewsets import ModelViewSet
from django_filters import FilterSet, NumberFilter

from apps.core.models import Item, Pedido
from apps.core.serializers import CreatePedidoSerializer, ItemSerializer, ListPedidoSerializer

class PedidoFilters(FilterSet):
    id_user = NumberFilter(field_name='id_user', lookup_expr='exact')

    class Meta:
        fields = ('id_user',)
        model = Pedido

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = ListPedidoSerializer
    filterset_class = PedidoFilters
    http_method_names = ['post', 'get']

    def get_serializer_class(self):
        if self.action == 'create':
            return CreatePedidoSerializer
        return CreatePedidoSerializer