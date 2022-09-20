from django.shortcuts import render
from django.shortcuts import HttpResponse


def Info(requset):
    return HttpResponse("This is Student info")