from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Occasion(models.Model):
    name = models.CharField(
        'Название причины сбора',
        max_length=55
    )

    class Meta:
        verbose_name = 'Повод для сбора'
        verbose_name_plural = 'Поводы для сбора'

    def __str__(self):
        return self.name


class Collect(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='collects',
        verbose_name='Автор сбора'
    )
    name = models.CharField(
        'Название',
        max_length=55
    )
    occasion = models.ForeignKey(
        Occasion,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Причина сбора'
    )
    description = models.TextField(
        'Описание'
    )
    amount = models.PositiveIntegerField(
        'Сумма сбора'
    )
    image = models.ImageField(
        'Обложка',
        upload_to='images/%Y/%M/%d'
    )
    date_of_end = models.DateField(
        'Дата завершения сбора'
    )

    class Meta:
        verbose_name = 'Сбор'
        verbose_name_plural = 'Сборы'

    def __str__(self):
        return self.name
