from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ...models import Classrooms
from ...serializers import ClassroomSerializer

class ClassroomViewSet(ModelViewSet):
    queryset = Classrooms.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["name"]
    lookup_field = "id"

    # def list(self, request):
    #     return self.list(request)
