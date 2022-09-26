from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    middle_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=200)
    date_of_birth = serializers.DateField()
    

class Meta:
    model = User
    fields = ('__all__')