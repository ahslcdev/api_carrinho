import factory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.LazyFunction(lambda: make_password('teste'))
    email = factory.Faker("email")