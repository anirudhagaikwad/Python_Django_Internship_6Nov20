from django.shortcuts import render,redirect
from website.forms import MyForm,ContactForm
from website.models import ContactInfo,IntroImg,PortProd2,PortProd3,PortProd1,Servi
from django.http import HttpResponse


# Create your views here.

def index_page(request):
    intro=IntroImg.objects.all()
    p1=PortProd1.objects.all()
    p2=PortProd2.objects.all()
    p3=PortProd3.objects.all()
    serv=Servi.objects.all()
    context={"heroimg":intro,"product1":p1,"product2":p2,"product3":p3,"services":serv}
    return render(request,"index.html",context)


def home_page(request):
    myname="Anirudha"
    return render(request,"webviews/index.html",{"my":myname})


def home_form(request):
    myf=MyForm()
    return render(request,"webviews/myform.html",{"mform":myf})


def contact(request):
    if request.method=="GET":
        cf=ContactForm()
    else:
        cf=ContactForm(request.POST)
        if cf.is_valid():
            try:
                cm=ContactInfo()
                cm.name=cf.cleaned_data['name']
                cm.gender=cf.cleaned_data['gender']
                cm.email=cf.cleaned_data['email']
                cm.mobile=cf.cleaned_data['mobile']
                cm.message=cf.cleaned_data['message']
                cm.save()
                return redirect('contact_form')
            except:
                return HttpResponse("Form Not Save ... Try Again")   
    return render(request,"webviews/contact.html",{"form":cf})

