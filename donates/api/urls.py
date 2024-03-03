from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.collects.views import CollectViewSet
from api.v1.payments.views import PaymentViewSet

from .schemas import schema_view

router_v1 = DefaultRouter()
router_v1.register('collect', CollectViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt')),
    path('collect/<int:id>/payments/', PaymentViewSet.as_view()),
    path('swagger/', schema_view.with_ui(cache_timeout=0)),
]
