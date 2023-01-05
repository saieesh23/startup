from django.contrib import admin
from django.urls import path, include
from myapp1 import views

urlpatterns = [ 
    path('',views.index, name="index"),
    path('login',views.loginuser, name="login"),
    path('register',views.register, name="register"),
    path('succesfull',views.succesfull, name="succesfull"),
    path('token',views.token, name="token"),
    path('home',views.home, name="home"),
    path('next',views.next, name="next"),
]
