from django.conf import settings
from django.core.cache import cache
from django.db.models import Sum, Count
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from collects.models import Occasion, Collect


class CollectListSerializer(ModelSerializer):
    class Meta:
        model = Collect
        fields = '__all__'


class CollectSerializer(ModelSerializer):
    occasion = PrimaryKeyRelatedField(
        queryset=Occasion.objects.all()
    )
    sum_payments = SerializerMethodField()
    count_of_payments = SerializerMethodField()

    class Meta:
        model = Collect
        fields = "__all__"

    def get_sum_payments(self, obj):
        cache_sum = cache.get(settings.SUM_PAYMENTS_CACHE)
        if cache_sum:
            sum_payments = cache_sum
        else:
            sum_payments = obj.payments.aggregate(sum_payments=Sum('amount'))
            cache.set(settings.SUM_PAYMENTS_CACHE, sum_payments, 30)
        return sum_payments

    def get_count_of_payments(self, obj):
        cache_count = cache.get(settings.COUNT_PAYMENTS_CACHE)
        if cache_count:
            count_payments = cache_count
        else:
            unique_names = obj.payments.values('name').distinct()
            count_payments = unique_names.aggregate(count_of_payments=(Count('name')))
            cache.set(settings.COUNT_PAYMENTS_CACHE, count_payments, 30)
        return count_payments
