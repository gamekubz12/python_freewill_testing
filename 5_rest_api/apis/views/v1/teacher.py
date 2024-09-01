from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from ...models import Teachers
from ...serializers import TeacherSerializer

class TeacherViewSet(ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
