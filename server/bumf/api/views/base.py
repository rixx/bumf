from django.conf import settings
from rest_framework import permissions, viewsets


class BumfViewSet(viewsets.ModelViewSet):
    """
    This base class allows the view to be displayed in the browsable API in DEBUG mode.
    """
    permission_classes = [
        permissions.AllowAny if settings.DEBUG else permissions.IsAuthenticated
    ]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return self.queryset.none()

        f = {self.user_relation: self.request.user}
        return self.queryset.filter(**f)
