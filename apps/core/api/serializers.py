from rest_framework.serializers import ModelSerializer, ListSerializer, ValidationError

from apps.core.models import Item, Pedido, PedidoItem

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def validate_preco(self, data):
        if data <= 0:
            raise ValidationError("Preço do item não pode ser menor ou igual a zero")
        return data

class PedidoItemSerializer(ModelSerializer):
    class Meta:
        fields = [
            'id_item',
            'quantidade'
        ]
        model = PedidoItem

    def validate_quantidade(self, data):
        if data <= 0:
            raise ValidationError("Quantidade de itens não pode ser menor ou igual a zero")
        return data

class PedidosSerializer(ModelSerializer):
    itens = ListSerializer(child=PedidoItemSerializer())

    class Meta:
        model = Pedido
        fields = [
            'id',
            'id_user', 
            'itens'
        ]

    def validate_itens(self, data):
        if not data:
            raise ValidationError('Não é possível realizar um pedido sem itens.')
        return data

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
        return pedido
    
    def to_representation(self, instance):
        retorno = super().to_representation(instance)
        retorno.pop('id_user')
        retorno['usuario'] = {
            "id": instance.id_user.id,
            "username": instance.id_user.username
        }
        return retorno