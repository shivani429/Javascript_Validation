from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

#javascript validation
def insert(request):
    return render(request,'insert.html')

