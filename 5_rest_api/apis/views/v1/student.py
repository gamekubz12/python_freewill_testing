from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from ...models import Students
from ...serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["name"]
    lookup_field = "id"
