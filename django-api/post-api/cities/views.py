from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema
from cities.models import City
from cities.serializers import CitySerializer

@extend_schema(tags=['Cities'])
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    parser_classes = [MultiPartParser, FormParser]
 