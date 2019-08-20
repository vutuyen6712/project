from django.urls import path
from . import views
from home.controllers.account.register import register_views 
from home.controllers.account.login import login_views 

urlpatterns = [
    path('',views.index, name="Home"),
    
    path('contact',views.contact, name="contact"),
   
    path('men/productgrid',views.men_productgrid, name="men product"),
    path('men/productlist',views.men_productlist, name="men productlist"),
    path('men/details',views.men_details, name="men details"),
    path('women/productgrid',views.women_productgrid, name="women product"),
    path('women/productlist',views.women_productlist, name="women productlist"),
    path('register',register_views.user_register, name="register"),
    path('login',login_views.user_login, name="login"),
]
