from myapp1.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def  index(request):
    return render(request, "index.html")


# Create your views here for register.
def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
    
       
        print(password)
        print(email)
        print(first_name)
        print(username)
        print(last_name)
        
        

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email , first_name = first_name , last_name = last_name  )
            user_obj.set_password(password)
            user_obj.save()

            auth_token = str(uuid.uuid4())
            print(str(uuid.uuid4()))

            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            
 
            return redirect('/token')

        except Exception as e:
            print(e)


    return render(request , 'register.html')


    # Create your views here for login.


    

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/home")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, "login.html") 


     # Create your views here for succesfull.

def  succesfull(request):
    return render(request, "succesfull.html")   


     # Create your views here for token.     

def  token(request):
    if request.user.is_anonymous:
        return redirect("/register")
    return render(request, "token.html")      


def  home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "home.html")   


def  next(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "next.html")   