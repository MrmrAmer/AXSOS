from django.shortcuts import render, redirect

def index(request):
    if 'view_count' not in request.session:
        request.session['view_count'] = 0
        request.session['counter'] = 0
    request.session['view_count'] += 1
    context = {
        "visits" : request.session['view_count'],
        "counter" : request.session['counter'],
    }
    return render(request, "index.html", context)

def increment(request):
    amount = int(request.POST['amount'])
    request.session['counter'] += amount
    return redirect('/')

def destroy(request):
    request.session.clear()
    return redirect('/')