from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView


from .views import alive_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alive', alive_view),
]

# graphql
urlpatterns += [path('graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True)))]
urlpatterns += [path('graphql/', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True)))]

# static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# rest api
urlpatterns += [path('boards/', include('boards.api.urls')),]

# rest api document
if settings.DEBUG:
    from drf_yasg.views import get_schema_view
    from django.urls import re_path
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="API",
            default_version='v1',
        ),
    )

    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    ]
