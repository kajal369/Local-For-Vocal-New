from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'signup/ragistration.html',{'name':'kajal','clg':'nitc'})
def index(request):
    data ={
        'name':'kaj','add':'burhan'
    }
    return render(request,'Dashboard/index.html',{'data':data})