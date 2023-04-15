from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import  CompanySerializer,EmployeeSerialaizer
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # Need to get url like - companies/<pk>/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(company_id=pk)
            emps = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerialaizer(emps,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            return Response({
                "message":"Company does not exists !"
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialaizer 