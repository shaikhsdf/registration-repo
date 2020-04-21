from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from registration_app.models import newUser
from django.urls import reverse
from django.contrib import auth, messages


def index(request):
    return render(request, 'registration_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('index')

def sucess(request):
    return render(request, 'registration_app/sucess.html')

def user_login(request):
      
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, usrname=username, password=password)
        
        if user:
            login(request, user)
            return HttpResponseRedirect('sucess')                       
        else:            
            return HttpResponse('Invalid Login Details')            
    else:
        return render(request, 'registration_app/login.html',{})



def loginpage(request):
    return render(request, "registration_app/login.html")