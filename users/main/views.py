from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
import requests
from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
# from themodels.models import Todo
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json



class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def TheModelView(request):

    if (request.method == "GET"):
        with open('/home/ezz/Documents/gitprojects/crediation/django_user/users/main/fixtures/people.json') as f:
            data = json.load(f) 
        # Turn the JSON data into a dict and send as JSON response
        # return JsonResponse(data, safe=False)
        return render(request = request,
                  template_name='main/home.html', 
                  context = {
   'data': data
    })
    return 

@csrf_exempt
def getName(request, name):
    with open(​'/home/ezz/Documents/gitprojects/crediation/django_user/users/main/fixtures/people.json') as jsonfile:
        json_data = json.load(json_file.read())
        json_data = filter(lambda​ ​x​: ​x​[​"name"​] ​==​ ​str​(​name​), ​json_data)
    return Response(json_data)