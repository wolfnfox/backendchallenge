from rest_framework import serializers
from ottoapi.models import Branch, Car, Driver

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id','city','postcode','capacity']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','registration','make','model','year',\
                  'currently_with','assigned_to','in_service','updated']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id','name','date_of_birth']