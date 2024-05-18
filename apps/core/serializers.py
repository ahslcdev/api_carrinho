from rest_framework.serializers import ModelSerializer, ListField, ListSerializer

from apps.core.models import Item, Pedido, PedidoItem

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PedidoItemSerializer(ModelSerializer):
    class Meta:
        fields = [
            'id_item',
            'quantidade'
        ]
        model = PedidoItem

class CreatePedidoSerializer(ModelSerializer):
    itens = ListSerializer(child=PedidoItemSerializer())

    class Meta:
        model = Pedido
        fields = [
            'id', 
            'id_user', 
            'itens'
        ]

    def create(self, validated_data):
        itens = validated_data.get('itens')
        validated_data.pop('itens')
        pedido = super().create(validated_data)
        list_itens = []
        for i in itens:
            list_itens.append(
                PedidoItem(id_item=i.get('id_item'), id_pedido=pedido, quantidade=i.get('quantidade'))
            )
        PedidoItem.objects.bulk_create(list_itens)
        print(pedido)
        return pedido
    
class ListPedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = [
            'id', 
            'id_user', 
            # 'itens'
        ]