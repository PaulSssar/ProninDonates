from django.conf import settings
from django.core.cache import cache


def cache_delete():
    cache.delete(settings.CACHE_LIST)
    cache.delete(settings.COUNT_PAYMENTS_CACHE)
    cache.delete(settings.SUM_PAYMENTS_CACHE)
    cache.delete(settings.CACHE_RETRIEVE)