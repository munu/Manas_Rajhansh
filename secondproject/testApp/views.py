from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(reqest):
	date=datetime.datetime.now()
	msg='<h1>Hello freind good Morning</h1>'
	msg=msg+'<h1>Server time is'+str(date)+'</h1>'
	return HttpResponse(msg)