from django.shortcuts import render

def index(request):
    
    return render(request, 'exp_one/index.html', {
        'Project Name': 'experiment_one',
    })

