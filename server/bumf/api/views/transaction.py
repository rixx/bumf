from django.db.models import Q

from bumf.api.serializers import (
    DossierSerializer, RealTransactionReadSerializer,
    RealTransactionWriteSerializer, VirtualTransactionReadSerializer,
)
from bumf.api.views.base import BumfViewSet
from bumf.core.models import Dossier, RealTransaction, VirtualTransaction


class DossierView(BumfViewSet):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    user_relation = 'project__user'


class VirtualTransactionView(BumfViewSet):
    queryset = VirtualTransaction.objects.all()
    serializer_class = VirtualTransactionReadSerializer
    user_relation = 'dossier__project__user'


class RealTransactionView(BumfViewSet):
    queryset = RealTransaction.objects.all()
    serializer_class = RealTransactionReadSerializer
    user_relation = 'dossier__project__user'

    def get_queryset(self):
        queryset = self.queryset
        account_id = self.request.query_params.get('account_id', None)
        if account_id is not None:
            queryset = queryset.filter(Q(source__id=account_id) | Q(destination__id=account_id))
        return queryset
