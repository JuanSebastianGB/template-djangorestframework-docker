from rest_framework import viewsets
from .models import Module, Student
from .serializer import ModuleSerializer, StudentSerializer


# Create your views here.
class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        module = self.request.query_params.get("module", None)
        if module is not None:
            queryset = queryset.filter(module=module)
        return queryset
