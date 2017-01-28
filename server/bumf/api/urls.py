from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views

from bumf.api.views import (
    DossierView, ProjectView, RealAccountView, RealTransactionView,
    UserView, VirtualAccountView, VirtualTransactionView,
)

from .signals import *  # noqa

router = routers.DefaultRouter()
router.register('dossier', DossierView)
router.register('project', ProjectView)
router.register('real-account', RealAccountView)
router.register('real-transaction', RealTransactionView)
router.register('register', UserView)
router.register('virtual-account', VirtualAccountView)
router.register('virtual-transaction', VirtualTransactionView)


urlpatterns = [
    url(regex=r'^v1/', view=include(router.urls)),
    url(regex=r'^token-auth/$', view=views.obtain_auth_token),
]
