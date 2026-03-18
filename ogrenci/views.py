from rest_framework import viewsets
from .models import Ogrenci
from .serializers import OgrenciSerializer

class OgrenciViewSet(viewsets.ModelViewSet):
    queryset = Ogrenci.objects.all()
    serializer_class = OgrenciSerializer