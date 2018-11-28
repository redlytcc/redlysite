from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .forms import Logred,CreateA
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
import json

User=get_user_model()


def log(request):
    if 'usuario' in request.session:
        return redirect('/redly/')
    if request.method == 'POST':
        form=Logred(request.POST)
        if form.is_valid():
            obb=form.cleaned_data
            usuario=obb['username']
            password=obb['password']
            if User.objects.filter(username=usuario):
                user=authenticate(username=usuario, password=password)
                print("auth",str(authenticate(username=usuario, password=password)))
                if user:
                    if user.is_active:
                        request.session['usuario']=usuario
                        login(request,user)
                        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form=Logred()
    context={
        'form':form
    }
    return render(request,'web/login.html',context)

def cada(request):
    if 'usuario' in request.session:
        return redirect('/redly/')
    if request.method == 'POST':
        form=CreateA(request.POST)
        if form.is_valid():
            form.save()
            forms=form.cleaned_data
            u=forms['username']
            p=forms['password1']
            user=authenticate(username=u, password=p)
            print("auth",str(authenticate(username=u, password=p)))
            print(user)
            print('\n')
            if user:
                if user.is_active:
                    request.session['usuario']=u
                    login(request,user)
                    return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form=CreateA()

    context={
        'form':form
    }
    return render(request,'web/create.html',context)

@login_required
def outred(request):
    logout(request)
    return redirect('/')

@login_required
def redhome(request):
    return render(request,'web/index2.html')

def homeinit(request):
    if 'usuario' in request.session:
        return redirect('/redly/')
    return render(request,"web/home.html")
