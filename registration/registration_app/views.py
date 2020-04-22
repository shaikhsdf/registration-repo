from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
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
        user = authenticate(request, username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('sucess')    
            else:
                return HttpResponse('Your Account is Not Active')                  
        else:
            msg = "Invalid Username / Password "            
            return render(request, 'registration_app/login.html',{"errormsg": msg})            
    else:
        return render(request, 'registration_app/login.html',{})
