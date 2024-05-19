from django_filters import FilterSet, NumberFilter

from apps.core.models import Pedido

class PedidoFilters(FilterSet):
    id_user = NumberFilter(field_name='id_user', lookup_expr='exact')
    
    class Meta:
        fields = ('id_user',)
        model = Pedido