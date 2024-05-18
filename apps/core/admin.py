from django.contrib import admin

from apps.core.models import Item, Pedido, PedidoItem

# Register your models here.
admin.site.register(PedidoItem)
# admin.site.register(Pedido)
admin.site.register(Item)

class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 0

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_user', 'criado_em',)
    inlines = (PedidoItemInline, )