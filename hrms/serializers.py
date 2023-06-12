from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class PayStubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paystub1
        fields = '__all__'

class create_time_off_request(serializers.ModelSerializer):
    class Meta:
        model = TimeOffRequest
        fields = '__all__'

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'
