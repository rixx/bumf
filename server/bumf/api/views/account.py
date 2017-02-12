from bumf.api.serializers import BudgetAccountSerializer, RealAccountSerializer
from bumf.api.views.base import BumfViewSet
from bumf.core.models import RealAccount, VirtualAccount, VirtualAccountVariants


class BudgetAccountView(BumfViewSet):
    queryset = VirtualAccount.objects.filter(variant=VirtualAccountVariants.BUDGET)
    serializer_class = BudgetAccountSerializer
    user_relation = 'project__user'


class RealAccountView(BumfViewSet):
    queryset = RealAccount.objects.all()
    serializer_class = RealAccountSerializer
    user_relation = 'project__user'
