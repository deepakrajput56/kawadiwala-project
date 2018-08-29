from django.shortcuts import render
from account import views

def home(request):
    return render(request,"account/home.html")
