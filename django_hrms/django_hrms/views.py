#-*-coding:utf-8 -*-
from django.shortcuts  import render,HttpResponseRedirect,render_to_response,HttpResponse
from django.contrib import auth  # 別忘了import auth

def login(request):

    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
  
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html') 

def base(request):
    return render_to_response('base.html',locals())


def index(request):
    return render_to_response('index.html',locals())

def test(req):

    return render_to_response('test.html',locals())


def profiles(request):
    
    user = request.user.in_employee_set.get(name = request.user )
    return render_to_response('profiles.html',locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')