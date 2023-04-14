from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import  CompanySerializer,EmployeeSerialaizer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialaizer 