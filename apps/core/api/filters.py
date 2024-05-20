from django_filters import FilterSet, NumberFilter, DateFilter

from apps.core.models import Pedido

class PedidoFilters(FilterSet):
    """
    Esta classe permite que seja possível realizar filtragem no model PEDIDO
    através dos campos informados.
    """
    id_user = NumberFilter(field_name='id_user', lookup_expr='exact', label='ID do usuário', )
    data_inicio = DateFilter(field_name='criado_em__date', lookup_expr='gte', label='Data inicial da criação do pedido')
    data_fim = DateFilter(field_name='criado_em__date', lookup_expr='lte', label='Data final da criação do pedido')

    class Meta:
        fields = [
            'id_user', 
            'data_inicio', 
            'data_fim',
        ]
        model = Pedido