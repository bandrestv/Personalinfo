# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Andrés Tapiero Vanegas: " + " For more Information U must log in as Admin" + " ;) ")

def obj_name(request, Label_id):
    return HttpResponse("You're looking for the information %s." % Label_id)

def st(request, Content_id):
    return HttpResponse("The information you are looking for is:  %s." % Content_id)