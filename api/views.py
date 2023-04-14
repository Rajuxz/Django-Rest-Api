from rest_framework import viewsets
from api.models import Company
from api.serializers import  CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

