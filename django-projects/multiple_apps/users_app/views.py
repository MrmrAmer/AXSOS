from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return redirect("/blogs")

def register(request):
    return HttpResponse("placeholder for users to create a new user record.")

def login(request):
    return HttpResponse("placeholder for users to log in.")

def users(request):
    return HttpResponse("placeholder to display all the list of users later.")