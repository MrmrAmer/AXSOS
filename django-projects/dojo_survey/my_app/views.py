from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')

def result(request):
    context = {
        "name_from_form": request.POST['name'],
        "location_from_form": request.POST['location'],
        "language_from_form": request.POST['language'],
        "comment_from_form": request.POST['comment'],
        "gender_from_form": request.POST.get('gender'),
        "accept_from_form": 'Yes' if request.POST.get('accept') else 'No'
    }
    return render(request,'show.html', context)