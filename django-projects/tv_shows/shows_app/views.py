from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(reqeust):
    return redirect("/shows")

def add(request):
    return render(request, "index.html")

def show(request, number):
    show = Show.objects.get(id=number)
    context = {
        'show' : show
    }
    return render(request, "show.html", context)

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request, "index.html", {"form_data": request.POST})
    
    else:

        if request.method == "POST":
            title = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['date']
            desc = request.POST['desc']

            show = Show.objects.create(
                title=title,
                network=network,
                release_date=release_date,
                desc=desc
            )
        messages.success(request, "Show successfully created!")
        return redirect(f'/shows/{show.id}')

def show_all(request):
    all_shows = Show.objects.all()
    context = {
        'shows' : all_shows
    }
    return render(request, "shows.html", context)

def edit(request, number):
    show = Show.objects.get(id=number)
    context = {
        'show': show
    }
    return render(request, "edit.html", context)

def update(request, number):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{number}/edit')

        show = Show.objects.get(id=number)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['date']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Show successfully updated!")

    return redirect(f'/shows/{show.id}')

def destroy(request, number):
    if request.method == "POST":
        show = Show.objects.get(id=number)
        show.delete()
    return redirect("/shows")