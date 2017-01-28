from bumf.api.serializers import RealAccountSerializer, VirtualAccountSerializer
from bumf.api.views.base import BumfViewSet
from bumf.core.models import RealAccount, VirtualAccount


class VirtualAccountView(BumfViewSet):
    queryset = VirtualAccount.objects.all()
    serializer_class = VirtualAccountSerializer
    user_relation = 'project__user'


class RealAccountView(BumfViewSet):
    queryset = RealAccount.objects.all()
    serializer_class = RealAccountSerializer
    user_relation = 'project__user'
