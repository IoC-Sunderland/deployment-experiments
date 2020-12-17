from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

try:
    STUB_USER = User.objects.create_user(username='Gavin', email='', password='TestPass')
    STUB_USER.save()
except: 
    pass


def index(request):
    
    if request.method == "POST":

        details = {}

        details['username'] = request.POST.get('username','')
        details['password'] = request.POST.get('password','')

        print(details)

        missing = list()

        for k, v in details.items():
            if v == "":
                missing.append(k)

        if missing:
            messages.add_message(
                request, messages.WARNING, f"Missing fields for {', '.join(missing)}")
            return render(request, "exp_one/index.html")

        # Check user exists
        user = authenticate(request, username=details['username'], password=details['password'])

        if user is not None:
            login(request, user)
            return render(request, "exp_one/welcome.html", {
            'username': details['username'],
            })
        else:
        # A backend did not authenticate
            messages.add_message(
                request, messages.WARNING, f"Invalid Credentials")
            return render(request, "exp_one/index.html")

    return render(request, "exp_one/index.html")


def signup(request):
    
    if request.method == "POST":
        
        details = {}

        details['username'] = request.POST.get('username','')
        details['email'] = request.POST.get('email', '')
        details['password'] = request.POST.get('password','')

        print(details)

        missing = list()

        for k, v in details.items():
            if v == "":
                missing.append(k)

        if missing:
            messages.add_message(
                request, messages.WARNING, f"Missing fields for {', '.join(missing)}")
            return render(request, "exp_one/sign-up.html")

        # Check user exists
        user = authenticate(request, username=details['username'], password=details['password'])
        print(user)

        if user is not None:
            login(request, user)
            return render(request, "exp_one/welcome.html", {
            'username': details['username'],
            })

        else:
            user = User.objects.create_user(username = details['username'],
                                             email = details['email'],
                                             password =  details['password'])

            user.save()
            login(request, user)
            return render(request, "exp_one/welcome.html", {
                'username': details['username'],
                })

    return render(request, "exp_one/sign-up.html")