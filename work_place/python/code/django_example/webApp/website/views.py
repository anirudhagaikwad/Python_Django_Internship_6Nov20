from django.shortcuts import render,redirect

# Create your views here.

def home_page(request):
    myname="Anirudha"
    return render(request,"webviews/index.html",{"my":myname})



