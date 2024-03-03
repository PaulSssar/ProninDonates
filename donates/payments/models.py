from django.db import models
from django.contrib.auth import get_user_model

from collects.models import Collect

User = get_user_model()


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='payments',
        on_delete=models.SET_NULL,
        null=True,
    )
    amount = models.PositiveIntegerField(
        'Сумма платежа'
    )
    date_of_payment = models.DateTimeField(
        'Дата платежа',
        auto_now_add=True
    )
    name = models.CharField(
        'ФИО',
        max_length=90
    )
    collect = models.ForeignKey(
        Collect,
        on_delete=models.CASCADE,
        verbose_name='Сбор',
        related_name='payments'
    )

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'{self.name} {self.date_of_payment} {self.amount}'
