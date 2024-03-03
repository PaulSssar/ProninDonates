from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ('https', 'http')
        return schema


schema_view = get_schema_view(
   openapi.Info(
      title='Donates API',
      default_version='v1',
      description=(
          'API для приложени я donates'
        ),
      terms_of_service='https://www.google.com/policies/terms/',
      license=openapi.License(name='BSD License'),
   ),
   generator_class=BothHttpAndHttpsSchemaGenerator,
   public=True,
   permission_classes=[permissions.AllowAny,],
)

LOGIN_SCHEMA = openapi.Schema(
   type=openapi.TYPE_OBJECT,
   required=['login', 'password',],
   properties={
      'login': openapi.Schema(type=openapi.TYPE_STRING),
      'password': openapi.Schema(type=openapi.TYPE_STRING),
   },
)
