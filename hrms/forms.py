from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class PayStubForm(forms.ModelForm):
    class Meta:
        model = Paystub1
        fields = '__all__'

class TimeOffRequestForm(forms.ModelForm):
    class Meta:
        model = TimeOffRequest
        fields = '__all__'


