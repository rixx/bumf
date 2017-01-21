from django.conf.urls import include, url

urlpatterns = [
    url(regex=r'^auth/', view=include('rest_framework.urls', namespace='rest_framework')),
    url(regex='', view=include('bumf.api.urls', namespace='api')),
]
