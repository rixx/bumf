from django.conf import settings
from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [url(r'^docs/$', get_swagger_view(title='bumf API'))] if settings.DEBUG else []
urlpatterns += [
    url(regex=r'^auth/', view=include('rest_framework.urls', namespace='rest_framework')),
    url(regex='', view=include('bumf.api.urls', namespace='api')),
]
