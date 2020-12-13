from django.shortcuts import render, redirect
from django.contrib import messages 

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

        new_user = Users(username=details['username'],
                         email=details['email'],
                        password=details['password'])

        print(new_user)

        new_user.save()

        return redirect('/')

    return render(request, "exp_one/index.html", {
        'Project Name': 'experiment_one',
    })

def welcome(request):

    return render(request, "exp_one/welcome.html")
