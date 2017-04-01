# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from restaurants.models import Restaurant
# Create your views here.
def menu(request):
	if id :
		r = Restaurant.objects.get(id=id)
		return render_to_response('menu.html',locals())
	else:
		return HttpResponseRedirect("/restaurant_list/")
def welcome(request):
	if 'user_name' in request.GET:
		return HttpResponse('Welcome~'+request.GET['user_name'])
	else:
		return render_to_response('welcome.html',locals())

def restaurant_list (request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurant_list.html',locals())