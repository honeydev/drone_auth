"""Root app URL Configuration."""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from drone_auth.views import index

schema_view = get_schema_view(
    openapi.Info(
        title='Drone auth API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^$', index, name='index'),
    path('admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT,
        ),
    )
