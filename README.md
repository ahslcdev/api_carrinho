### API Carrinho

## Tecnologias Utilizadas
- Django e REST framework
- PostgreSQL
- Docker

## Funcionalidades Implementadas
- Cadastrar usuários
- Login
- Logout
- Atualizar token refresh
- Atualizar informações de usuários
- Listar todos os usuários
- Listar usuário específico
- Cadastrar itens
- Atualizar informações de itens
- Excluir item
- Listar todos os itens
- Listar item específico
- Criar novo pedido
- Listar todos os pedidos
- Listar todos os pedidos de um usuário
- Listar pedido específico

## Como rodar o projeto e os testes sem o Docker
1. Clone este repositório: `git clone https://github.com/ahslcdev/api_carrinho`
2. Navegue até o diretório do projeto: `cd api_carrinho`
3. Crie o ambiente virtual: `python -m venv venv`
4. Ative o ambiente 
    * Linux: `source venv/bin/activate`
    * Windows: `cd venv/bin/activate`
                `cd ../../`
5. Instale as dependências: `pip install -r requirements.txt`
6. Altere o nome do arquivo `.env.example` para `.env`
7. Aplique as migrações: `python manage.py migrate`
8. Crie um super usuário: `python manage.py createsuperuser`
9. Execute os testes: `python manage.py test tests`
10. Inicie o servidor: `python manage.py runserver`

## Como rodar o projeto e os testes com Docker
1. Certifique-se de ter o Docker instalado na sua máquina.
2. Clone este repositório: `git clone https://github.com/ahslcdev/api_carrinho`
3. Navegue até o diretório do projeto: `cd api_carrinho`
4. Altere o nome do arquivo `.env.example.docker` para `.env`
5. Construa a imagem do Docker e inicie os serviços: `docker compose up -d --build`
6. Crie um super usuário: `docker exec -it api python manage.py createsuperuser`
7. Execute os testes: `docker exec -it api python manage.py test tests`

## Informações adicionais
- O preço do item foi salvo como inteiro pois dessa forma não teria problemas no retorno dos dados no endpoint.
- O projeto utiliza de uma biblioteca que não permite a criação de senhas fracas para os usuários, exceto ao rodar o comando `python manage.py createsuperuser`
- A documentação do projeto encontra-se na url `http://localhost:<PORT>/api/schema/swagger-ui/`
- Através da url fornecida acima, é possível realizar todas as requisições HTTP através da tela disponibilizada.
    - Para realizar as chamadas HTTP é necessário autenticar
- Para rodar o projeto com DOCKER, deve-se criar um env file com as variáveis presentes no arquivo .env.example.docker
- Para rodar o projeto sem DOCKER, deve-se criar um env file com as variáveis presentes no arquivo .env.example