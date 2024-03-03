from datetime import datetime
from random import randint

import factory
from django.contrib.auth import get_user_model
from faker import Faker

from collects.models import Collect

from .models import Payment

faker = Faker()
User = get_user_model()


def get_user():
    count = User.objects.count()
    user = User.objects.get(id=randint(1, count))
    return user


def get_collect():
    count = Collect.objects.count()
    collect = Collect.objects.get(id=randint(1, count))
    return collect


class PaymentsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment

    user = factory.LazyFunction(get_user)
    amount = factory.Faker(
        provider='pyint',
        min_value=1,
        max_value=100000,
    )
    date_of_payment = factory.Faker(
        provider='date_between',
        start_date=datetime.now()
    )
    name = factory.Faker(
        provider='name',
        locale='ru_RU'
    )
    collect = factory.LazyFunction(get_collect)
