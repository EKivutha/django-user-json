from rest_framework_json_api import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name','age', 'address')

