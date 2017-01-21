from rest_framework import viewsets

from bumf.api.serializers import RealAccountSerializer, VirtualAccountSerializer
from bumf.core.models import RealAccount, VirtualAccount


class VirtualAccountView(viewsets.ModelViewSet):
    serializer_class = VirtualAccountSerializer
    queryset = VirtualAccount.objects.all()


class RealAccountView(viewsets.ModelViewSet):
    serializer_class = RealAccountSerializer
    queryset = RealAccount.objects.all()
