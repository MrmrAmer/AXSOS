from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
 
def index(request):
    context = {
        "time1": strftime("%b %d, %Y", gmtime()),
        "time2": strftime("%I:%M %p", gmtime()),
    }
    return render(request,'index.html', context)