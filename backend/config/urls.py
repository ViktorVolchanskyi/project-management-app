from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('apps.api.urls', namespace='api')),
    path('', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
    # enable media on localhost
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.SHOW_DOCS:
    from rest_framework import permissions

    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Backend API",
            default_version='v1'
        ),
        public=True,
        permission_classes=(permissions.AllowAny,)
    )

    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=None),
             name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=None),
             name='schema-redoc'),
    ]
