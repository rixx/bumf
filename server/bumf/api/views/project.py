from bumf.api.serializers import ProjectSerializer
from bumf.api.views.base import BumfViewSet
from bumf.core.models import Project


class ProjectView(BumfViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    user_relation = 'user'
