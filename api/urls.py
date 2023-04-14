from django.urls import path,include
from rest_framework import routers
from api.views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)


urlpatterns = [
    path('', include(router.urls)),  
]
