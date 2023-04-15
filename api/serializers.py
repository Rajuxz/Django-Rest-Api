from rest_framework import serializers
from api.models import Company,Employee
# Create serializers.
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerialaizer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"