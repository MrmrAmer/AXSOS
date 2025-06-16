from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "dojos": Dojo.objects.all()
    }
    return render(request, "index.html", context)

def add_dojo(request):
    if request.method == "POST":
        name = request.POST.get("name")
        city = request.POST.get("city")
        state = request.POST.get("state")
        Dojo.objects.create(name=name, city=city, state=state)
    return redirect('/')

def add_ninja(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dojo_id = request.POST.get("dojo_id")
        dojo = Dojo.objects.get(id=dojo_id)
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('/')

def delete_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('/')