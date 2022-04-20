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
        if response['response']:
            request.session['isregistration']=False
            request.session['islfvuserlogin']=True
            request.session['lfvloginstatus']=response['status']
            request.session['lfvusername']=response['name']
            request.session['lfvuseremail']=response['email']
            request.session['lfvusermobile']=response['mobile']
            request.session['lfvuserstate']=response['state']
            request.session['lfvusercity']=response['city']
            request.session['lfvuserlcity']=response['lcity']
            request.session['islfvuserbusiness']=response['business']
            request.session['lfvuserprofile']=response['avatar']
            request.session['lfvusercountry']=response['country']
            islogin=True
            userdata = {
                'name':request.session['lfvusername'],
                'email':request.session['lfvuseremail'],
                'mobile':request.session['lfvusermobile'],
                'state':request.session['lfvuserstate'],
                'city':request.session['lfvusercity'],
                'Lcity':request.session['lfvuserlcity'],
                'isbusiness':request.session['islfvuserbusiness'],
                'avatar':request.session['lfvuserprofile'],
                'country':request.session['lfvusercountry']
            }
            return render(request,'Dashboard/index.html',{'userdata':userdata})
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
    if 'islfvuserlogin' in request.session:
        if request.session['islfvuserlogin']:
            islogin=True
            userdata = {
                'name':request.session['lfvusername'],
                'email':request.session['lfvuseremail'],
                'mobile':request.session['lfvusermobile'],
                'state':request.session['lfvuserstate'],
                'city':request.session['lfvusercity'],
                'Lcity':request.session['lfvuserlcity'],
                'isbusiness':request.session['islfvuserbusiness'],
                'avatar':request.session['lfvuserprofile'],
                'country':request.session['lfvusercountry']
            }
            url = utils.makeup_url('crudbusiness.py')
            payload = {'req':'getAllBusiness','mobile':request.session['lfvusermobile']}
            AllBusiness = requests.post(url,data=payload).json()
            return render(request,'Dashboard/index.html',{'userdata':userdata,'AllBusiness':AllBusiness})
        else:
            return render(request,'signup/login.html',{'iserror':iserror,'msg':msg,'LoginStatus':'0'})        
    else:
        return render(request,'signup/login.html',{'iserror':iserror,'msg':msg,'LoginStatus':'0'})        
def index(request):
    if 'islfvuserlogin' in request.session:
        if request.session['islfvuserlogin']:
            userdata = {
                'name':request.session['lfvusername'],
                'email':request.session['lfvuseremail'],
                'mobile':request.session['lfvusermobile'],
                'state':request.session['lfvuserstate'],
                'city':request.session['lfvusercity'],
                'Lcity':request.session['lfvuserlcity'],
                'isbusiness':request.session['islfvuserbusiness'],
                'avatar':request.session['lfvuserprofile'],
                'country':request.session['lfvusercountry']
            }
            url = utils.makeup_url('crudbusiness.py')
            payload = {'req':'getAllBusiness','mobile':request.session['lfvusermobile']}
            AllBusiness = requests.post(url,data=payload).json()
            return render(request,'Dashboard/index.html',{'userdata':userdata,'AllBusiness':AllBusiness})
        else:
            return redirect('login')
    else:
        return redirect('login')

def business(request):
    if 'islfvuserlogin' in request.session:
        if request.session['islfvuserlogin']:
            userdata = {
                'name':request.session['lfvusername'],
                'email':request.session['lfvuseremail'],
                'mobile':request.session['lfvusermobile'],
                'state':request.session['lfvuserstate'],
                'city':request.session['lfvusercity'],
                'Lcity':request.session['lfvuserlcity'],
                'isbusiness':request.session['islfvuserbusiness'],
                'avatar':request.session['lfvuserprofile'],
                'country':request.session['lfvusercountry']
            }
            url = utils.makeup_url('crudbusiness.py')
            payload = {'req':'getAllBusiness','mobile':request.session['lfvusermobile']}
            AllBusiness = requests.post(url,data=payload).json()
            return render(request,'Business/viewbusiness.html',{'userdata':userdata,'AllBusiness':AllBusiness})
        else:
            return redirect('login')
    else:
        return redirect('login')

def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('login')


def profile(request):
    if 'islfvuserlogin' in request.session:
        if request.session['islfvuserlogin']:
            userdata = {
                'name':request.session['lfvusername'],
                'email':request.session['lfvuseremail'],
                'mobile':request.session['lfvusermobile'],
                'state':request.session['lfvuserstate'],
                'city':request.session['lfvusercity'],
                'Lcity':request.session['lfvuserlcity'],
                'isbusiness':request.session['islfvuserbusiness'],
                'avatar':request.session['lfvuserprofile'],
                'country':request.session['lfvusercountry']
            }

            url = utils.makeup_url('crudbusiness.py')
            payload = {'req':'getAllBusiness','mobile':request.session['lfvusermobile']}
            AllBusiness = requests.post(url,data=payload).json()
            return render(request,'signup/profile.html',{'userdata':userdata,'AllBusiness':AllBusiness})
        else:
            return redirect('login')
    else:
        return redirect('login')
def newbusiness(request):
    if 'islfvuserlogin' in request.session:
        if request.session['islfvuserlogin']:

            
            if request.method == "POST" and  request.POST.get('req') == 'AddNewCategory':
                print('Inside AddNewCategory function')
                url = utils.makeup_url('crudbusiness.py')
                payload = {'req':'addcategory','category':request.POST.get('category'),'type':request.POST.get('type')}
                response = requests.post(url,data=payload).json()
                return JsonResponse({'data':response},status=200)
            if request.method == "POST" and  request.POST.get('req') == 'GetBusinessCategory':
                #print(" inside GetBusinessCategory function")
                AllCategory = getAllBusinessCategory()
                #print(AllCategory)
                return JsonResponse({'data':AllCategory},status=200)
            if request.POST and request.POST.get('req') == 'AddBusiness':
                mobile = request.session['lfvusermobile']
                logo=request.POST.get('logo')
                Bname=request.POST.get('Bname')
                Bemail=request.POST.get('Bemail')
                Btype=request.POST.get('Btype')
                Bcategory=request.POST.get('Bcategory')
                Boptime=request.POST.get('Boptime')
                Bcltime=request.POST.get('Bcltime')
                timing = str(Boptime)+' to '+str(Bcltime)
                BDesc=request.POST.get('BDesc')
                url = utils.makeup_url('crudbusiness.py')
                payload = {'req':'addbusiness','mobile':mobile,'name':Bname,'category':Bcategory,'image':logo,'timing':timing,'email':Bemail,'promotion':BDesc,'type':Btype}
                response = requests.post(url,data=payload).json()
                return JsonResponse({'data':response},status=200)
            return render(request,'Business/AddnewBusiness.html')
        else:
            return redirect('login')
    else:
        return redirect('login')

def registration(request):
    if request.method == "POST" and 'register' in request.POST:
        print('inside register')
        request.session['tempmobile']=request.POST.get('hiddenno')
        request.session['tempemail']=request.POST.get('emailadd')
        request.session['tempprofile']=request.POST.get('imgurl')
        request.session['tempname']=request.POST.get('name')
        request.session['tempcountry']=request.POST.get('country')
        request.session['tempstate']=request.POST.get('state')
        request.session['tempcity']=request.POST.get('city')
        request.session['tempLcity']=request.POST.get('Lcity')
        request.session['temppassword']=request.POST.get('password')
        url = utils.makeup_url('cruduser.py')
        payload = {'req':'checksignup','mobile':request.POST.get('hiddenno')}
        response = requests.post(url, data = payload).json()
        if response['response']:
            iserror = True
            errormsg = "Mobile Number Already Registered"
            progressstep = {"step1":True,"step2":False,"step3":False,"step4":False}
            return render(request,'signup/registration.html',{'progress':progressstep,'iserror':iserror,'errormsg':errormsg,'AllCategory':AllCategory})
        else:
            randomtop = randomN(6)
            request.session['tempotp'] = randomtop
            mobileno = request.session['tempmobile']
            url = utils.getotp_url(str(mobileno),str(randomtop))
            print('mobile no is {0} otp is {1} url is {2}'.format(mobileno,randomtop,url))
            payload = ""
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.request("GET", url, data=payload, headers=headers)
            response = response.json()
            iserror = False
            errormsg = "NA"
            progressstep = {"step1":False,"step2":True,"step3":False,"step4":False}
            return render(request,'signup/registration.html',{'progress':progressstep,'iserror':iserror,'errormsg':errormsg,})

    if request.method == "POST" and 'verifyotpbtn' in request.POST:
        userotp = request.POST.get('formotp')
        print('send otp ',request.session['tempotp'])
        print('user otp ',userotp)
        if str(userotp) == str(request.session['tempotp']):
            #print('otp matched')
            url = utils.makeup_url("cruduser.py")
            payload={'req':'NewRegistration','mobile':request.session['tempmobile'],'name':request.session['tempname'],'avatar':request.session['tempprofile'],'email':request.session['tempemail'],'country':request.session['tempcountry'],'state':request.session['tempstate'],'city':request.session['tempcity'],'Lcity':request.session['tempLcity'],'password':request.session['temppassword']}
            response=requests.post(url,data=payload).json()
            #print('response',response)
            if(response['status']):
                request.session['isregistration']=False
                request.session['islfvuserlogin']=True
                request.session['lfvusername']=request.session['tempname']
                request.session['lfvuseremail']=request.session['tempemail']
                request.session['lfvusermobile']=request.session['tempmobile']
                request.session['lfvuserprofile']=request.session['tempprofile']
                request.session['lfvusercountry']=request.session['tempcountry']
                request.session['lfvuserstate']=request.session['tempstate']
                request.session['lfvusercity']=request.session['tempcity']
                request.session['lfvuserlcity']=request.session['tempLcity']
                request.session['islfvuserbusiness']='0'
                islogin=True
                return redirect('index')
            else:
                request.session['isregistration']=True
                islogin=False
                pagestep = {'step1':True,'step2':False}
                return render(request,'Registration/registration.html',{'iserror':True,'errormsg':response['message'],'pagestep':pagestep})
        else:
            #print('otp not matched')
            pagestep = {'step1':False,'step2':True}
            return render(request,'Registration/registration.html',{'iserror':True,'errormsg':"Otp not matcheds!",'pagestep':pagestep,})
        

    iserror = False
    errormsg = "NA"            
    progressstep = {"step1":True,"step2":False,"step3":False,"step4":False}
    return render(request,'signup/registration.html',{'progress':progressstep,'iserror':iserror,'errormsg':errormsg,})

def getAllBusinessCategory():
    url = utils.makeup_url('crudbusiness.py')
    payload = {'req':'getallcategory'}
    response = requests.post(url,data=payload).json()
    return response

def randomN(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
