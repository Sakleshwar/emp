from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import *
from .serializers import *
from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import *
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
# class EmployeeUpdateAPIView(APIView):
@api_view
def EmployeeUpdateAPIPostView(request):
    try:
        if request.method == 'POST':
            try:
                
                a = request.body
                b = json.load(a)
                b = b['id']
                b = b['fName']
                b = b['lName']
                b = b['email']
                b = b['desig']
                b = b['add']
                
                Emp = Employee.objects.get(pk=b)
                
                First_name         = (Emp.first_name)
                Last_name           = (Emp.last_name)
                Email             = (Emp.email)
                Designation        = (Emp.designation)
                Address         = (Emp.address)

                
                Emp.first_name            = First_name
                Emp.last_name              = Last_name
                Emp.email             = Email
                Emp.designation        = Designation
                Emp.address         = Address
                

                Emp.save()
                # userUpdate = Employee(id = id,first_name,lName,email = email,designation = desig, address= add)
                return JsonResponse({"status":"success"})
            
            except Exception as ex:
                return JsonResponse({"status":"failed"})
            
    except Exception as ex:
        return ex
@api_view
def PayStubCreateAPIView(request):
    try:
        if request.method == "POST":
            try:
                a = request.body
                b = json.load(a)
                b = b['id']
                b = b['pay_period_start']
                b = b['pay_period_end']
                b = b['gross_earnings']
                b = b['overtime_earnings']
                b = b['pre_tax_deductions']
                b = b['federal_income_tax']
                b = b['state_income_tax']
                b = b['post_tax_deductions']
                b = b['employer_contribution']
                b = b['net_pay']
                
                Pay_stub = Paystub1.objects.get(pk=b)
                
                Period_start         = (Pay_stub.pay_period_start)
                Period_end           = (Pay_stub.pay_period_end)
                Gross_earnings             = (Pay_stub.gross_earnings)
                Overtime_earnings        = (Pay_stub.overtime_earnings)
                Pre_tax_deductions         = (Pay_stub.pre_tax_deductions)
                Federal_income_tax         = (Pay_stub.federal_income_tax)
                State_income_tax         = (Pay_stub.state_income_tax)
                Post_tax_deductions         = (Pay_stub.post_tax_deductions)
                Employer_contribution         = (Pay_stub.employer_contribution)
                Net_pay         = (Pay_stub.net_pay)

                
                Pay_stub.pay_period_start            = Period_start
                Pay_stub.pay_period_end              = Period_end
                Pay_stub.gross_earnings             = Gross_earnings
                Pay_stub.overtime_earnings        = Overtime_earnings
                Pay_stub.pre_tax_deductions         = Pre_tax_deductions
                Pay_stub.federal_income_tax         = Federal_income_tax
                Pay_stub.state_income_tax         = State_income_tax
                Pay_stub.post_tax_deductions         = Post_tax_deductions
                Pay_stub.employer_contribution         = Employer_contribution
                Pay_stub.net_pay         = Net_pay
                
                # usr = Paystub1(id = id, employee=emp, pay_period_start=stdate, pay_period_end=enddate, gross_earnings=grossearning, overtime_earnings=ot, pre_tax_deductions=pretax, federal_income_tax=fdincome, state_income_tax=stincome,post_tax_deductions=posttax,employer_contribution=emplrcontrbtn,net_pay=netpay)
                Pay_stub.save()
                
                return JsonResponse({"status":"success"})
            
            except Exception as ex:
                return JsonResponse({"status":"failed"})

    except Exception as ex:
        print(ex)

@csrf_exempt
@api_view(['POST'])
def timeOffRequest(request):
    
    serializer = create_time_off_request(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': 'Time off request created'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])

def policy_list_create(request):
    if request.method == 'GET':
        
        policies = Policy.objects.all()
        serializer = PolicySerializer(policies, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PolicySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])

def policy_retrieve_update_destroy(request):
    try:
        content = json.loads(request.body.decode('utf-8'))
        id = content['id']
        title = content['title']
        contentt = content['content']
        createAt = int(datetime.strptime((content['createdAt']), "%Y-%m-%d %H:%M:%S"))
        updateAt =int(datetime.strptime((content['updatedAt']), "%Y-%m-%d %H:%M:%S"))
        policyy = Policy.objects.get(pk=id)
        policyy.title = title
        policyy.content = contentt
        policyy.created_at = createAt
        policyy.updated_at = updateAt
        policyy.save()
        dataSaving = ("policyy.title","policyy.content","policyy.created_at","policyy.updated_at")
        print("bvduibur")
    except Exception as dataSaving:
        return dataSaving

    if request.method == 'GET':
        serializer = PolicySerializer(Policy)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = PolicySerializer(Policy, data=request.method, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        Policy.delete()
        return Response(status=204)