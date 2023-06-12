from django.urls import path
from .views import *

# app_name = 'hrms'

urlpatterns = [
    path('employee/update', EmployeeUpdateAPIPostView, name='employee-update'),
    path('paystub/create', PayStubCreateAPIView, name='paystub-create'),
    path('timeoff/request', create_time_off_request, name='create_time_off_request'),
    path('api/policies/', policy_retrieve_update_destroy, name='policy-list-create'),
]
