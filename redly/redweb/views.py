from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Chat
from webapimd.forms import FormChat
import json

@login_required
def redhome(request):
    allmsm=Chat.objects.order_by('-id').filter(visible=1)[:30]
    Last=Chat.objects.values_list('id').order_by('-id')[:1]
    l=int()
    for i in Last:
        l=i[0]

    if l=='':
        l=0
    print(l)
    us = request.session['usuario']
    form=FormChat()
    context={
        'us':us,
        'form':form,
        'Last':l,
        'allmsm':allmsm,
    }
    return render(request,'web/index2.html',context)

@csrf_exempt
@login_required
def removeChat(request,id):
    if Chat.objects.filter(id=id).exists():
        Chat.objects.filter(id=id).update(visible=0)
    return HttpResponse('ok')
