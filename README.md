### API

## Como rodar o projeto e os testes sem o Docker
1. Clone este repositório: `git clone https://github.com/ahslcdev/api_carrinho`
2. Navegue até o diretório do projeto: `cd api_carrinho`
3. Crie o ambiente virtual: `python -m venv venv`
4. Ative o ambiente 
    * Linux: `source venv/bin/activate`
    * Windows: `cd venv/bin/activate`
                `cd ../../`
5. Instale as dependências: `pip install -r requirements.txt`
6. Aplique as migrações: `python manage.py migrate`
7. Crie um super usuário: `python manage.py createsuperuser`
8. Execute os testes: `python manage.py test tests`
9. Inicie o servidor: `python manage.py runserver`

## Como rodar o projeto e os testes com Docker

1. Certifique-se de ter o Docker instalado na sua máquina.
2. Clone este repositório: `git clone https://github.com/ahslcdev/api_carrinho`
3. Navegue até o diretório do projeto: `cd api_carrinho`
4. Construa a imagem do Docker e inicie os serviços: `docker compose up -d --build`
5. Crie um super usuário: `docker exec -it api python manage.py createsuperuser`
6. Execute os testes: `docker exec -it api python manage.py test tests`