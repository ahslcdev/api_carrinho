from rest_framework.routers import DefaultRouter

from apps.core.viewsets import ItemViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'itens', ItemViewSet)
router.register(r'pedidos', PedidoViewSet)