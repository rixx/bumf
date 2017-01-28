from bumf.api.serializers import RealAccountSerializer, VirtualAccountSerializer
from bumf.api.views.base import BumfViewSet
from bumf.core.models import RealAccount, VirtualAccount


class VirtualAccountView(BumfViewSet):
    serializer_class = VirtualAccountSerializer
    queryset = VirtualAccount.objects.all()


class RealAccountView(BumfViewSet):
    serializer_class = RealAccountSerializer
    queryset = RealAccount.objects.all()
