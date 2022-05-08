from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse_lazy

from .forms import UserRegisterForm

# Create your views here.


def login(request):
    if request.method == "POST":
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponse("<h1>Logged in</h1>")
        else:
            context = {
                "error_message": "Username or password is incorrect",
            }

            return render(request, 'users/error.html', context)

    form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'users/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('login_page')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            print("User registered")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(f'Account created for {username}!')

            user = authenticate(request, username=username, password=password)

            auth_login(request, user)

            return HttpResponse("<h1>Registered and logged in</h1>")
        else:
            context = {
                "error_message": "Error registering a user."
            }

            return render(request, 'users/error.html', context)

    form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'users/register.html', context)


def not_found_page(request, exception):
    return render(request, 'users/404.html')


def not_found_page_server(request):
    return render(request, 'users/404.html')


def thank_you(request):
    return render(request, "users/thankyou.html")
