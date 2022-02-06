from django.shortcuts import render, redirect
from django.http import HttpResponse
import json,requests
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from random import randint
from API import config,utils

# Create your views here.
def login(request):
    pagesteps={'step1':False,'step2':True,}
    if request.method == "POST" and 'sendotp' in request.POST:
        print('send otp function is called')
        mobileno=request.POST.get('hiddenno')
        otp = randomN(6)
        url = utils.getotp_url(str(mobileno),str(otp))
        print('mobile no is {0} otp is {1} url is {2}'.format(mobileno,otp,url))
        payload = ""
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.request("GET", url, data=payload, headers=headers)
        response = response.json()
        print(response)
        if response['Status'] == 'Success':
            pagesteps1={'step1':False,'step2':True,}
            return render(request,'signup/login.html',{'pagesteps':pagesteps1,'sendOTP':otp,'mobileno':mobileno})
    return render(request,'signup/login.html',{'pagesteps':pagesteps})
def index(request):
    data ={
        'name':'kaj','add':'burhan'
    }
    return render(request,'Dashboard/index.html',{'data':data})
def ragistration(request):
    return render(request,'signup/ragistration.html')

def randomN(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
