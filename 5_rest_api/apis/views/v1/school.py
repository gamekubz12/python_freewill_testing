from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from ...models import School
from ...serializers import SchoolSerializer, ClassroomSerializer

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]
