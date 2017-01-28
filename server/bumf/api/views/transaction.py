from bumf.api.serializers import (
    DossierSerializer, RealTransactionSerializer, VirtualTransactionSerializer,
)
from bumf.api.views.base import BumfViewSet
from bumf.core.models import Dossier, RealTransaction, VirtualTransaction


class DossierView(BumfViewSet):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    user_relation = 'project__user'


class VirtualTransactionView(BumfViewSet):
    queryset = VirtualTransaction.objects.all()
    serializer_class = VirtualTransactionSerializer
    user_relation = 'dossier__project__user'


class RealTransactionView(BumfViewSet):
    queryset = RealTransaction.objects.all()
    serializer_class = RealTransactionSerializer
    user_relation = 'dossier__project__user'
