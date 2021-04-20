from django.shortcuts import render,HttpResponse,redirect
from .models import Travel_details
from datetime import datetime, date
from django.contrib import messages 

from django.core.mail import send_mail
from django.conf import settings

# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags


def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

# travel form

def travel_form(request):
    return render(request,'traveler_form.html')

def traveler_details(request):


    place=request.POST['place']
    # print(place)
    from_date=request.POST['from_date']
    # print(type(from_date),from_date)

    
    y,m,d=list(map(int,from_date.split("-")))
    # print(y,m,d)
    d1= date(y,m,d)

    current_time = datetime.now()
    d2 = date(current_time.year,current_time.month,current_time.day)

    diff_days= (d1-d2)
    print(diff_days)
    # print(type(diff_days))
    
    travel=Travel_details(
        place=place,
        username=request.POST['name'],
        address=request.POST['address'],
        email=request.POST['email'],
        phone=request.POST['phone'],
        from_date=from_date,
        no_people=request.POST['no_people'],
        adult=request.POST['adult'],
        children=request.POST['children'],

    )
    print(travel)
    
    
    # print(name)
    # print(address)
    # print(email)
    # print(phone)
    # print(no_people)
    # print(adult)
    # print(children)

    

    if place=="tadoba" and diff_days.days > 60:
        print("tadoba")
        print(diff_days)
        travel.save()

    

    elif place=="kabini" and diff_days.days > 15:
        print('kabni')
        print(diff_days)
        travel.save()
  
    elif place=='bharatpur' and diff_days.days > 2:
        print('bird')
        print(diff_days)
        travel.save()

    else:
        print("please choose appropriate date") 
        messages.info(request,'please choose appropriate date ')

    return render(request,'traveler_form.html')



def book_views(request):
    traveler=Travel_details.objects.all()
    context={'traveler':traveler}
    return render(request,'traveler_detail.html',context)



def edit(request,id):
    
    traveler=Travel_details.objects.get(id=id)
    
    context={'traveler':traveler}
    return render(request,'edit.html',context)

def emailform(request,id):
    traveler=Travel_details.objects.get(id=id)
    
    context={'traveler':traveler}
    
    return render(request,'email.html',context)    


def sendemail(request):
    if request.method=="POST":
        to=request.POST.get('toemail')
        content=request.POST.get('content')
        # print(to,content)
        send_mail(
            #subject
            "testing",
            #message
            content,
            #fromemail
            settings.EMAIL_HOST_USER,
            #recepient list
            [to]
        )
        return redirect('/book_views',{'title':'testing','content':content})

    else:
        return render(request,'email.html',{'title':'testing','content':content})
