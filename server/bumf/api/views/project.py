from rest_framework import viewsets

from bumf.api.serializers import ProjectSerializer
from bumf.core.models import Project


class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
