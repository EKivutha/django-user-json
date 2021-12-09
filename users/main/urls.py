from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
   path('',include(router.urls)),
   
]
