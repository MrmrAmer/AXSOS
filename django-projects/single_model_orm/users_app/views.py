from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    context = {
        "all_the_users": User.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email_address']
    age = request.POST['age']

    User.objects.create(
        first_name=first_name,
        last_name=last_name,
        email_address=email,
        age=int(age)
    )
    return redirect('/')
    