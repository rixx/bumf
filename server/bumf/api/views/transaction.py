from bumf.api.serializers import (
    DossierSerializer, RealTransactionSerializer, VirtualTransactionSerializer,
)
from bumf.api.views.base import BumfViewSet
from bumf.core.models import Dossier, RealTransaction, VirtualTransaction


class DossierView(BumfViewSet):
    serializer_class = DossierSerializer
    queryset = Dossier.objects.all()


class VirtualTransactionView(BumfViewSet):
    serializer_class = VirtualTransactionSerializer
    queryset = VirtualTransaction.objects.all()


class RealTransactionView(BumfViewSet):
    serializer_class = RealTransactionSerializer
    queryset = RealTransaction.objects.all()
