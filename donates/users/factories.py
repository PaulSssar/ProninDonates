import factory
from django.contrib.auth import get_user_model
from faker import Faker

User = get_user_model()
faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker(provider='user_name')
    password = factory.Faker(provider='password')
