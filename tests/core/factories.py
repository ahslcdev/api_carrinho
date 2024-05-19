import factory
from apps.core.models import Pedido
from tests.autenticacao.factories import UserFactory

class PedidoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pedido

    id_user = factory.SubFactory(UserFactory)