from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views

from bumf.api.views import (
    DossierView, ProjectView, RealAccountView, RealTransactionView,
    UserView, VirtualAccountView, VirtualTransactionView,
)

from .signals import *  # noqa

router = routers.DefaultRouter()
router.register('dossiers', DossierView)
router.register('projects', ProjectView)
router.register('real-accounts', RealAccountView)
router.register('real-transactions', RealTransactionView)
router.register('register', UserView)
router.register('virtual-accounts', VirtualAccountView)
router.register('virtual-transactions', VirtualTransactionView)


urlpatterns = [
    url(regex=r'^v1/', view=include(router.urls)),
    url(regex=r'^token-auth/$', view=views.obtain_auth_token),
]
