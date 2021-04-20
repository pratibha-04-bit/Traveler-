
from django.urls import path
from . import views


urlpatterns = [
     path('index',views.index,name="index"),
     path('home',views.home,name="home"),

     path('travel_form',views.travel_form, name="travel_form"),
     path('traveler_details',views.traveler_details, name="traveler_details"),
     # path('booking_views',views.booking_views, name="booking_views"),
     path('book_views',views.book_views, name="book_views"),
     #path('confirm_booking/<int:id>/<str:email>',views.confirm_booking, name="confirm_booking"),
     #path('emailDetail/<int:id>',views.emailDetail, name="emailDetail"),
     
     path('edit/<int:id>',views.edit,name='edit'),
     path('emailform/<int:id>',views.emailform,name='emailform'),
     path('emailform/sendemail',views.sendemail,name='sendemail')


    
     

   
]
