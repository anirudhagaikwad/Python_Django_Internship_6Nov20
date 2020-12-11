from django.shortcuts import render,redirect
from website.forms import MyForm,ContactForm


# Create your views here.

def home_page(request):
    myname="Anirudha"
    return render(request,"webviews/index.html",{"my":myname})


def home_form(request):
    myf=MyForm()
    return render(request,"webviews/myform.html",{"mform":myf})


def contact(request):
    cf=ContactForm()
    return render(request,"webviews/contact.html",{"contactForm":cf})

