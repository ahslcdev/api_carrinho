from typing import Any
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from tests.autenticacao.factories import UserFactory

class UsuarioViewSetTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = UserFactory()
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.url_base = '/autenticacao'
        return super().setUp()
    
    def test_http_sem_auth(self):
        """
        Este teste tem por objetivo provar que não é possível acessar
        os endpoints sem autenticação
        """
        response_list = self.client.get(f"{self.url_base}/api/usuarios/")
        self.assertEqual(response_list.status_code, 401)

        response_retrieve = self.client.get(f"{self.url_base}/api/usuarios/123/")
        self.assertEqual(response_retrieve.status_code, 401)

        response_post = self.client.post(f"{self.url_base}/api/usuarios/")
        self.assertEqual(response_post.status_code, 401)

        response_put = self.client.put(f"{self.url_base}/api/usuarios/123/")
        self.assertEqual(response_put.status_code, 401)

        response_patch = self.client.patch(f"{self.url_base}/api/usuarios/123/")
        self.assertEqual(response_patch.status_code, 401)

    def test_get_success(self):
        """
        Teste de sucesso ao acessar o endpoint de listagem de usuários
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(f"{self.url_base}/api/usuarios/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_get_especifico_success(self):
        """
        Teste de sucesso ao acessar o endpoint de get especifico do usuário
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(f"{self.url_base}/api/usuarios/{self.user.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), dict)
        self.assertEqual(response.json().get('username'), self.user.username)

    def test_get_especifico_error(self):
        """
        Teste de sucesso ao acessar o endpoint de get especifico do usuário
        que não existe
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(f"{self.url_base}/api/usuarios/1000/")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(type(response.json()), dict)

    def test_post_success(self):
        """
        Teste de sucesso ao tentar cadastrar um novo usuário
        """
        data = {
            "username": "teste",
            "password": "teste",
            "email": "teste@gmail.com"
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(f"{self.url_base}/api/usuarios/", data)
        self.assertEqual(response.status_code, 201)
        self.assertGreaterEqual(len(response.json()), 2)

    def test_post_error_username(self):
        """
        Teste de erro ao tentar cadastrar um usuário com username já existente
        """
        data = {
            "username": self.user.username,
            "password": "teste",
            "email": "teste@gmail.com"
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(f"{self.url_base}/api/usuarios/", data)
        self.assertEqual({'username': ['Um usuário com este nome de usuário já existe.']}, response.json())
        self.assertEqual(response.status_code, 400)

    def test_post_error_blank(self):
        """
        Teste de erro ao tentar cadastrar um usuário com username ou password
        em branco
        """
        data = {
            "username": '',
            "password": "teste",
            "email": 'teste@example.com'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(f"{self.url_base}/api/usuarios/", data)
        self.assertEqual({'username': ['Este campo não pode ser em branco.']}, response.json())
        self.assertEqual(response.status_code, 400)

        data = {
            "username": 'teste2',
            "password": "",
            "email": 'teste@example.com'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(f"{self.url_base}/api/usuarios/", data)
        self.assertEqual({'password': ['Este campo não pode ser em branco.']}, response.json())
        self.assertEqual(response.status_code, 400)

    def test_patch_success(self):
        """
        Teste de sucesso ao atualizar os dados de um usuário
        """
        username_antigo = self.user.username
        data = {
            "username": 'teste5'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.patch(f"{self.url_base}/api/usuarios/{self.user.id}/", data)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json().get('username'), username_antigo)

    def test_patch_error_username(self):
        """
        Teste de error ao atualizar o username de um usuário colocando
        um username já existente
        """
        new_user = UserFactory()
        data = {
            "username": new_user.username
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.patch(f"{self.url_base}/api/usuarios/{self.user.id}/", data)
        self.assertEqual(response.status_code, 400)


class AutenticacaoTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = UserFactory()
        self.token = RefreshToken.for_user(self.user)
        self.url_base = '/autenticacao'
        return super().setUp()
    
    def test_login_success(self):
        """
        Teste de sucesso ao efetuar o login com todos os dados corretos
        """
        data = {
            'username': self.user.username,
            'password': 'teste'
        }
        response = self.client.post(f"{self.url_base}/login/", data)
        self.assertEqual(response.status_code, 200)

    def test_login_error_invalid_data(self):
        """
        Teste de error ao tentar efetuar o login com o username errado
        """
        data = {
            'username': '123',
            'password': 'teste'
        }
        response = self.client.post(f"{self.url_base}/login/", data)
        self.assertEqual(response.status_code, 401)

    def test_logout_success(self):
        """
        Teste de sucesso ao efetuar o logout
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        data = {
            'refresh': str(self.token)
        }
        response = self.client.post(f"{self.url_base}/logout", data)
        self.assertEqual(response.status_code, 200)

    def test_logout_error(self):
        """
        Teste de error ao tentar efetuar o logout com um token refresh errado
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        data = {
            'refresh': '123'
        }
        response = self.client.post(f"{self.url_base}/logout", data)
        self.assertEqual(response.status_code, 401)

    def test_refresh_success(self):
        """
        Teste de sucesso ao obter um novo token refresh
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        data = {
            'refresh': str(self.token)
        }
        response = self.client.post(f"{self.url_base}/refresh/", data)
        self.assertEqual(response.status_code, 200)

    def test_refresh_error(self):
        """
        Teste de error ao tentar obter um novo token refresh informando um token inválido
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        data = {
            'refresh': '123'
        }
        response = self.client.post(f"{self.url_base}/refresh/", data)
        self.assertEqual(response.status_code, 401)