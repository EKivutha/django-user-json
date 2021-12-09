from rest_framework import serializers
#from .models import User

class UserSerializer(serializers.Serializer):
   index = Serializers.IntegerFiled()
   isActive = Serializers.BooleanFiled()
   picture = Serializers.CharFiled()
   age = Serializers.IntegerFiled()
   gender = Serializers.CharFiled()
   email = Serializers.CharField()
   phome = Serializers.CharField()

