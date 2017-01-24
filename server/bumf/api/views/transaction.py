from rest_framework import viewsets

from bumf.api.serializers import (
    DossierSerializer, RealTransactionSerializer, VirtualTransactionSerializer,
)
from bumf.core.models import Dossier, RealTransaction, VirtualTransaction


class DossierView(viewsets.ModelViewSet):
    serializer_class = DossierSerializer
    queryset = Dossier.objects.all()


class VirtualTransactionView(viewsets.ModelViewSet):
    serializer_class = VirtualTransactionSerializer
    queryset = VirtualTransaction.objects.all()


class RealTransactionView(viewsets.ModelViewSet):
    serializer_class = RealTransactionSerializer
    queryset = RealTransaction.objects.all()
