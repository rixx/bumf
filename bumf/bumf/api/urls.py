from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views

from .signals import *  # noqa

router = routers.DefaultRouter()


urlpatterns = [
    url(regex=r'^v1/', view=include(router.urls)),
    url(regex=r'^token-auth/$', view=views.obtain_auth_token),
]
