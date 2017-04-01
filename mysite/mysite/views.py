# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
def here(request):
	#return HttpResponse('MOM,! I AM HERE!')
	return HttpResponse('妈，我在这里！')

def math(request,a,b):
	
	a = float(a)
	b = float(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b 

	return render_to_response('math.html',locals())

