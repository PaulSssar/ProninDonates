from django.conf import settings
from django.core.cache import cache
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsOwnerOrReadOnly
from api.tasks import send_email_to
from api.utils import cache_delete
from collects.models import Collect

from .serializers import CollectListSerializer, CollectSerializer


class CollectViewSet(ModelViewSet):
    serializer_class = CollectSerializer
    queryset = Collect.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        cache_delete()
        send_email_to.delay('Сбор',
                      f'Создан сбор',
                      'example@yandex',
                      ('example@yandex', )
                      )
        user = self.request.user
        serializer.save(user=user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CollectListSerializer
        return CollectSerializer

    def list(self, request, *args, **kwargs):
        cache_list = cache.get(settings.CACHE_LIST)
        response = super().list(request, *args, **kwargs)
        if cache_list:
            response.data = cache_list
        else:
            cache.set(settings.CACHE_LIST, response.data, 30)
        return response

    def retrieve(self, request, *args, **kwargs):
        cache.delete()
        collect_id = self.kwargs.get('pk')
        cache_retrieve = cache.get(settings.CACHE_RETRIEVE + collect_id)
        response = super().retrieve(request, *args, **kwargs)
        if cache_retrieve:
            response.data = cache_retrieve
        else:
            cache.set(settings.CACHE_RETRIEVE + collect_id, response.data, 30)
        return response
