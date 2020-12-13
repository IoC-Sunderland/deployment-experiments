from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

STUB_USER = User.objects.create_user(username='Gavin', email='', password='TestPass')
STUB_USER.save()


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
        user = authenticate(username=details['username'],
                             password=details['password'])

        if user is not None:
        # A backend authenticated the credentials
            return render(request, "exp_one/welcome.html", {
            'username': details['username'],
            })

        else:
        # A backend did not authenticate
            return render(request, "exp_one/user_does_not_exist.html", {
                'username': details['username'],
             })

        return render(request, "exp_one/welcome.html", {
        'username': details['username'],
    })

    return render(request, "exp_one/index.html")

def welcome(request):

    return render(request, "exp_one/welcome.html")
