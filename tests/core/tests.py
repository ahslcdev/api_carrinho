import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from model_bakery import baker

from apps.core.models import Item, Pedido
from tests.autenticacao.factories import UserFactory
from tests.core.factories import PedidoFactory

class ItensTesteCase(TestCase):
    def setUp(self) -> None:
        self.client_not_auth = APIClient()
        self.client_auth = APIClient()
        self.user = UserFactory()
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client_auth.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.url_base = '/core'

        self.item = baker.make(Item)
        return super().setUp()
    
    def test_http_sem_auth(self):
        """
        Este teste tem por objetivo provar que não é possível acessar
        os endpoints sem autenticação
        """
        response_list = self.client_not_auth.get(f"{self.url_base}/itens/")
        self.assertEqual(response_list.status_code, 401)

        response_retrieve = self.client_not_auth.get(f"{self.url_base}/itens/123/")
        self.assertEqual(response_retrieve.status_code, 401)

        response_post = self.client_not_auth.post(f"{self.url_base}/itens/")
        self.assertEqual(response_post.status_code, 401)

        response_delete = self.client_not_auth.delete(f"{self.url_base}/itens/123/")
        self.assertEqual(response_delete.status_code, 401)

        response_patch = self.client_not_auth.patch(f"{self.url_base}/itens/123/")
        self.assertEqual(response_patch.status_code, 401)

    def test_list_success(self):
        response = self.client_auth.get(f"{self.url_base}/itens/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_retrieve_success(self):
        response = self.client_auth.get(f"{self.url_base}/itens/{self.item.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('id'), self.item.id)

    def test_retrieve_error(self):
        response = self.client_auth.get(f"{self.url_base}/itens/1500000000/")
        self.assertEqual(response.status_code, 404)

    def test_post_success(self):
        data = {
            "preco": 150,
            "nome": "teste"
        }
        response = self.client_auth.post(f"{self.url_base}/itens/", data)
        self.assertEqual(response.status_code, 201)

    def test_post_error_blank(self):
        data = {
            "preco": '',
            "nome": "teste"
        }
        response = self.client_auth.post(f"{self.url_base}/itens/", data)
        self.assertEqual(response.status_code, 400)

    def test_post_error_preco_zero(self):
        data = {
            "preco": 0,
            "nome": "teste"
        }
        response = self.client_auth.post(f"{self.url_base}/itens/", data)
        self.assertEqual(response.status_code, 400)

    def test_patch_success(self):
        data = {
            "nome": "teste2"
        }
        response = self.client_auth.patch(f"{self.url_base}/itens/{self.item.id}/", data)
        self.assertEqual(response.status_code, 200)

    def test_patch_error_preco_zero(self):
        data = {
            "preco": 0
        }
        response = self.client_auth.patch(f"{self.url_base}/itens/{self.item.id}/", data)
        self.assertEqual(response.status_code, 400)

    def test_delete_success(self):
        total_antes = Item.objects.all().count()
        response = self.client_auth.delete(f"{self.url_base}/itens/{self.item.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertGreater(total_antes, Item.objects.all().count())

    def test_delete_error(self):
        response = self.client_auth.delete(f"{self.url_base}/itens/1233333/")
        self.assertEqual(response.status_code, 404)


class PedidoTestCase(TestCase):
    def setUp(self) -> None:
        self.client_not_auth = APIClient()
        self.client_auth = APIClient()
        self.user = UserFactory()
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client_auth.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.url_base = '/core'
        baker.make(Item, 5)
        self.pedido = PedidoFactory()
        return super().setUp()
    
    def test_http_sem_auth(self):
        """
        Este teste tem por objetivo provar que não é possível acessar
        os endpoints sem autenticação
        """
        response_list = self.client_not_auth.get(f"{self.url_base}/pedidos/")
        self.assertEqual(response_list.status_code, 401)

        response_retrieve = self.client_not_auth.get(f"{self.url_base}/pedidos/123/")
        self.assertEqual(response_retrieve.status_code, 401)

        response_post = self.client_not_auth.post(f"{self.url_base}/pedidos/")
        self.assertEqual(response_post.status_code, 401)

    def test_list_success(self):
        response = self.client_auth.get(f"{self.url_base}/pedidos/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_retrieve_success(self):
        response = self.client_auth.get(f"{self.url_base}/pedidos/{self.pedido.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('id'), self.pedido.id)

    def test_retrieve_error(self):
        response = self.client_auth.get(f"{self.url_base}/pedidos/1500000000/")
        self.assertEqual(response.status_code, 404)

    def test_post_success(self):
        data = {
            "id_user": self.user.id,
            "itens": [
                {
                    "id_item": i.id,
                    "quantidade": 5
                }
                for i in Item.objects.all()
            ]
        }
        response = self.client_auth.post(f"{self.url_base}/pedidos/", json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertGreater(Pedido.objects.all().count(), 1)

    def test_post_error(self):
        data = {
            "id_user": self.user.id,
            "itens": []
        }
        response = self.client_auth.post(f"{self.url_base}/pedidos/", json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)