from django.db import models
from django.contrib.auth.models import User

from apps.base_models import BaseModels

class Item(BaseModels):
    nome = models.CharField(max_length=255, verbose_name='Nome do item')
    preco = models.IntegerField(verbose_name='Valor do item')
    ativo = models.BooleanField(verbose_name='Ativo?', default=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'


class Pedido(BaseModels):
    id_user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    @property
    def itens(self):
        lista = [
            {
                "id_item": i.id_item,
                'quantidade': i.quantidade
            }
            for i in PedidoItem.objects.filter(id_pedido__id=self.id)
        ]
        return lista


class PedidoItem(BaseModels):
    id_item = models.ForeignKey(Item, on_delete=models.SET_NULL, verbose_name='Item', null=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, verbose_name='Pedido', null=True)
    quantidade = models.IntegerField(default=1, verbose_name='Quantidade de itens')

    class Meta:
        verbose_name = 'Pedido e Item'
        verbose_name_plural = 'Pedidos e Itens'