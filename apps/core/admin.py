from django.contrib import admin

from apps.core.models import Item, Pedido, PedidoItem

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'ativo', 'criado_em',)

class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_user', 'criado_em',)
    inlines = (PedidoItemInline, )