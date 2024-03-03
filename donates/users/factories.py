import factory

from faker import Faker
from django.contrib.auth import get_user_model

User = get_user_model()
faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker(provider='user_name')
    password = factory.Faker(provider='password')
