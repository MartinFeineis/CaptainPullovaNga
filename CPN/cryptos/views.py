from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Pullova says: \"Babe is really sorry. But it is better now.\"")
# Create your views here.

def lbstatus(request):
	return HttpResponse("Everything okay")
