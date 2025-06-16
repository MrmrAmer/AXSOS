from django.shortcuts import render, redirect
import random

def index(request):
    if 'randomNum' not in request.session:
        request.session['randomNum'] = random.randint(1, 100)
        request.session['attempts'] = 0
        print(request.session['randomNum'])
    return render(request,'index.html')

def random_number(request):
    request.session['attempts'] += 1
    num=int(request.POST['random_number'])
    if request.session['attempts'] >= 5 and num != request.session['randomNum']:
        context = {
            'result': "You Lose",
            'attempts': request.session['attempts']
        }
        return render(request,'index.html',context)
    
    if num < request.session['randomNum']:
        context = {
            'result': "Too low!",
            'attempts': request.session['attempts']
            }
        return render(request,'index.html',context)
    elif num > request.session['randomNum']:
        context = {
            'result': "Too high!",
            'attempts': request.session['attempts']
            }
        return render(request,'index.html',context)
    elif num == request.session['randomNum']:
        context = {
            'result': True,
            'num': num,
            'attempts': request.session['attempts']
        }
        return render(request,'index.html',context)
    
leaderboard = []    
def leader(request):
    request.session['name'] = request.POST['name']
    leaderboard.append({
        'name': request.session['name'], 
        'attempts': request.session['attempts']
        })
    return redirect('/leaderboard')

def show_leaderboard(request):
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x['attempts'])
    context = {
    'leaderboard': sorted_leaderboard
    }
    return render(request,'leaderboard.html',context)

def reset(request):
    request.session.clear()
    return redirect('/')