from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def newApp(request):
    return render(request,"app_form/add_new.html")
