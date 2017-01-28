from rest_framework import mixins, permissions, viewsets

from bumf.api.serializers import UserSerializer
from bumf.core.models import User


class UserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.none()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
