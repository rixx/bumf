from bumf.api.serializers import ProjectSerializer
from bumf.api.views.base import BumfViewSet
from bumf.core.models import Project


class ProjectView(BumfViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
