from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from django.utils import timezone
from .forms import LoginForm, SignUpForm
from .models import accounts


# Create your views here.

def login(request):
    login_form = LoginForm(request.POST or None)
    signup_form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    messages.success(request, "You have been securely logged in")
                    return redirect("home-page")
                else:
                    messages.success(request, "The password is valid, but the account has been disabled!"
                                              " Please contact Tom (+91 999 50 600 98) or mail : cto@technorip.com")
                    return redirect("mylogin")
            else:
                messages.success(request, "The username and password were incorrect.")
                return redirect("mylogin")
        else:
            messages.success(request, "The username and password were invalid.")
            return redirect("mylogin")

    context = {"Form": login_form, "SignUpForm": signup_form
               }
    return render(request, 'login.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(request.POST)
        if form.is_valid():
            FirstName = form.cleaned_data.get("first_name")
            LastName = form.cleaned_data.get("last_name")
            Email = form.cleaned_data.get("email")
            Gender = form.cleaned_data.get("gender")
            Username = form.cleaned_data.get("username")
            Password = form.cleaned_data.get("password")
            MobileNo = form.cleaned_data.get("mobile")
            Dob = form.cleaned_data.get("dob")
            NewUser = User.objects.create_user(Username, Email, Password)
            #NewUser.first_name = FirstName
            NewUser.last_name = LastName
            NewUser.is_active = False
            NewUser.save()
            NewAccount = accounts(date_of_birth=Dob,gender=Gender,mobile_no=MobileNo)
            NewAccount.save()
            messages.success(request, "Hi,%s ! You have been Succesfully Signed Up, Please Login Again " % (FirstName))
            return render(request, "home.html", {})
        else:
            messages.success(request, "Sorry you have submitted wrong or invalid informations!.")
            return redirect("home-page")

    return redirect("home-page")


def home(request):
    messages.success(request, "you have been entered  Succesfully")
    return render(request, 'home.html', {})


def signup(request):
    messages.success(request, "message from signup view")
    return render(request, 'home.html', {})
