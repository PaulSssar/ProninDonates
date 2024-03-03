from datetime import datetime
from random import randint

import factory
from django.contrib.auth import get_user_model
from faker import Faker

from .models import Collect, Occasion

fake = Faker()
User = get_user_model()


def get_occasion():
    count = Occasion.objects.count()
    occasion = Occasion.objects.get(id=randint(1, count))
    return occasion


def get_user():
    count = User.objects.count()
    user = User.objects.get(id=randint(1, count))
    return user


class CollectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Collect
    author = factory.LazyFunction(get_user)
    name = factory.Faker(provider='word', locale='ru_RU')
    occasion = factory.LazyFunction(get_occasion)
    description = factory.Faker(
        provider='text',
        locale="ru_RU",
        max_nb_chars=200)
    amount = factory.Faker(
        provider='pyint',
        min_value=100,
        max_value=1000000000
    )
    image = factory.Faker(
        provider='file_path',
        category='image'
    )
    date_of_end = factory.Faker(
        provider='date_between',
        start_date=datetime.now()
    )
