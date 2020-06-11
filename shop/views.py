from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import person

def index(request, slug):
    obj=person.objects.all()
    chk=0
    slug=slug.casefold()
    for x in obj:
        ur=x.firstname[0:3]+x.phone[0:3]
        print(ur)
        ur=ur.casefold()
        if(ur==slug):
            ur=ur.casefold()
            chk=1
            break
    if(chk==1):
        return render(request,'show.html',{'z':x})
    else:
        return HttpResponse("Enter the url in the form of msg.iloveimpact.com/persons/first_three_letters_of_firstnam+first_three_digits_of_your_mobilenumber ")

def gaumata(request, slug):
    obj=person.objects.all()
    chk=0
    slug=slug.casefold()
    for x in obj:
        ur=x.firstname[0:3]+x.phone[0:3]
        print(ur)
        ur=ur.casefold()
        if(ur==slug):
            ur=ur.casefold()
            chk=1
            break
    if(chk==1):
        return render(request,'cow.html',{'z':x})
    else:
        return HttpResponse("Enter the url in the form of msg.iloveimpact.com/persons/first_three_letters_of_firstnam+first_three_digits_of_your_mobilenumber ")
