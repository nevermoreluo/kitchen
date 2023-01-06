"""

"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

from kitchen.rest import rest_router
from django.views.generic import TemplateView
# import services.rest

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/', include(rest_router.urls)),
    # path(r'api-auth/', include('rest_framework.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'services/', include('services.urls')),
    path(r'admin/', admin.site.urls),

    # Route TemplateView to serve Swagger UI template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
            title="Kitchen",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),
]
