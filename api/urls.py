from django.urls import path,include
from rest_framework import routers
from api.views import CompanyViewSet,EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employee',EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)), 
]
