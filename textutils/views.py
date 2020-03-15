from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
    params={'name':'ram','value':12}
    return render(request,"index.html",params)

    #return HttpResponse("hey tej")

def about(request):
    return HttpResponse("aabout ")

def help(request):
    tej=request.GET.get("text","default")
    print(tej)
    params={'name':tej,'value':24}
    #return HttpResponse("done")
    return render(request,"index.html",params)