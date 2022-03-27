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
    if request.method == "POST" and 'VerifyMobilePass' in request.POST:
        print('VerifyMobilePass function is called')
        mobileno=request.POST.get('hiddenno')
        password=request.POST.get('hiddenpass')
        url = utils.makeup_url('cruduser.py')
        payload = {'req':'checklogin','mobile':mobileno,'password':password}
        print(payload)
        response = requests.post(url,data=payload).json()
        print(response)
        if response['response']:
            request.session['islfvuserlogin']=True
            request.session['lfvloginstatus']=response['status']
            request.session['lfvusername']=response['name']
            request.session['lfvuseremail']=response['email']
            request.session['lfvusermobile']=response['mobile']
            request.session['lfvuserstate']=response['state']
            request.session['lfvuserdist']=response['dist']
            request.session['lfvusercity']=response['city']
            request.session['lfvuserlcity']=response['lcity']
            request.session['islfvuserbusiness']=response['business']
            return redirect('index')
        elif response['status']=='2':
            request.session['lfvloginstatus']=response['status']
            request.session['islfvuserlogin']=False
            iserror = True
            msg = "Password Not Matched"
            return render(request,'signup/login.html',{'iserror':iserror,'msg':msg,'LoginStatus':request.session['lfvloginstatus']})        
        elif response['status']=='3':
            request.session['lfvloginstatus']=response['status']
            request.session['islfvuserlogin']=False
            iserror = True
            msg = "Mobile Number not Registered"
            return render(request,'signup/login.html',{'iserror':iserror,'msg':msg,'LoginStatus':request.session['lfvloginstatus']})        
    iserror = False
    msg = ""
    return render(request,'signup/login.html',{'iserror':iserror,'msg':msg,'LoginStatus':'0'})        
def index(request):
    data ={
        'name':'kaj','add':'burhan'
    }
    return render(request,'Dashboard/index.html',{'data':data})
def ragistration(request):
    if request.method == "POST" and 'register' in request.POST:
        request.session['tempmobile']=request.POST.get('hiddenno')
        request.session['tempemail']=request.POST.get('hiddenno')
        request.session['tempprofile']=request.POST.get('hiddenno')
        request.session['tempname']=request.POST.get('hiddenno')
        request.session['tempcountry']=request.POST.get('hiddenno')
        request.session['tempstate']=request.POST.get('hiddenno')
        request.session['tempcity']=request.POST.get('hiddenno')
        request.session['tempLcity']=request.POST.get('hiddenno')
        url = utils.makeup_url('cruduser.py')
        payload = {'req':'checksignup','mobile':request.POST.get('hiddenno')}
        response = request.post(url,data=payload)
        if response['response']:
            iserror = True
            msg = "Mobile Number Already Registered"
            progressstep = {"step1":False,"step2":False,"step3":False,"step4":True}
            return render(request,'signup/ragistration.html',{'progress':progressstep})
        else:
            
    progressstep = {"step1":True,"step2":False,"step3":False,"step4":False}
    return render(request,'signup/ragistration.html',{'progress':progressstep})

def randomN(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
