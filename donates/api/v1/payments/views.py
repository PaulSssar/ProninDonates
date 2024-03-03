from django.core.cache import cache
from djoser.conf import settings
from rest_framework.generics import CreateAPIView
from .serializers import PaymentSerializer
from payments.models import Payment
from api.utils import cache_delete

from ...tasks import send_email_to


class PaymentViewSet(CreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self, id):
        queryset = Payment.objects.filter(collect__id=id)
        return queryset

    def perform_create(self, serializer):
        pk = self.kwargs.get('id')
        cache_delete()
        cache.delete(settings.CACHE_RETRIEVE + pk)
        send_email_to.delay('Оплата',
                            f'Оплата прошла успешно!',
                            'example@yandex',
                            ('example@yandex',))
        user = self.request.user
        pk = self.kwargs.get('id')
        if user.is_authenticated:
            serializer.save(user=user, collect_id=pk)
        else:
            serializer.save(user=None, collect_id=pk)
