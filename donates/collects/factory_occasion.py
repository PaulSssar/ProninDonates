import factory
from django.contrib.auth import get_user_model
from faker import Faker

from .models import Occasion

fake = Faker()
User = get_user_model()


class OccasionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Occasion

    name = factory.Faker(provider='job', locale='ru_RU')
