from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from django.utils import timezone
from .forms import LoginForm, SignUpForm


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
        # print(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            gender = form.cleaned_data.get("gender")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.date_joined = timezone.now()
            user.is_active = False
            user.save()
            NewAccount = accounts()
            NewAccount.user = user
            NewAccount.gender = gender
            NewAccount.save()
            messages.success(request, "Hi,%s ! You have been Succesfully Signed Up, Please Login Again " % (first_name))
            return render(request, "home.html", {})
        else:
            messages.success(request, "Sorry you have submitted wrong or invalid informations!.")
            return redirect("mysite:login-page")

    return redirect("mysite:login-page")


def home(request):
    messages.success(request, "you have been entered  Succesfully")
    return render(request, 'home.html', {})


def signup(request):
    messages.success(request,"message from signup view")
    return render(request, 'home.html', {})
