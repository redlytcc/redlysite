from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from core.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from redweb.models import Chat
from .forms import FormChat
import json

User=get_user_model()

@csrf_exempt
def home(request):
    if request.body==b'':
        return redirect("/")
    a=json.loads(request.body)
    if User.objects.filter(username=a['username']):
        user = authenticate(username=a['username'],password=a['password'])
        if user:
            if user.is_active:
                resposta=a['username']
                return JsonResponse({'user':resposta})
    else:
        return JsonResponse({'user':'Dont existed'})

@csrf_exempt
def cad(request):
    # print('hello')
    if request.body==b'':
        return redirect("/")
    # print(request.body)
    a=json.loads(request.body)
    # print(a)
    email=a['email']
    usuario=a['username']
    resposta=[]
    if User.objects.filter(email=email).exists():
        resposta.append("Esse email já existe tente outro")
    if User.objects.filter(username=usuario).exists():
        resposta.append(" Esse usuario já existe tente outro")

    if resposta==[]:
        cadastro=User(name=a['name'],email=a['email'],username=a["username"],password=a["password"])
        cadastro.save()
        tcad=User.objects.get(username=usuario)
        tcad.set_password(a["password"])
        tcad.save()
        resposta='OK'
        return JsonResponse({'user':resposta})
    else:
        return JsonResponse({'user':resposta})


@csrf_exempt
def gtPost(request,lsd=-1):
    resposta=[]
    if lsd == -1:
        a=Chat.objects.order_by('-id').filter(visible=1)[:30]
    else:
        a=Chat.objects.filter(visible=1).filter(id__gt=lsd)
    for i in a:
        x=[]
        x.append(i.id)
        x.append(i.nome)
        if i.img:
            x.append('/media/'+str(i.img))
        else:
            x.append(str(i.img))
        x.append(str(i.text))
        x.append(str(i.date))
        resposta.append(x)
    return JsonResponse({'u':resposta})


@csrf_exempt
def ptPost(request):
    if request.method == "POST":
        form=FormChat(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return JsonResponse({'a':'b'})
