from rest_framework.viewsets import ModelViewSet
from .models import Department
from .serializers import DepartmentSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
@extend_schema(tags=['Departments'])
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    parser_classes = [MultiPartParser, FormParser]
 