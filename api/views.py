from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def home(request):
    friends = ["uttam","utsav","pawan"]
    return JsonResponse(friends,safe=False)
