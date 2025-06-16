from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['moves'] = 0
        request.session['status'] = None
    context = {
        "gold" : request.session['gold'],
        "activities" : request.session['activities'],
        "moves" : request.session['moves'],
        "status" : request.session['status'],
        "max_moves": request.session.get('max_moves', 15),
        "target_gold": request.session.get('target_gold', 500),
    }
    return render(request,'index.html', context)

def process(request, building):
    if 'status' in request.session and request.session['status'] is not None:
        return redirect('/')
    
    gold_earned = 0
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")

    if building == 'farm':
        gold_earned = random.randint(10, 20)
    elif building == 'cave':
        gold_earned = random.randint(5,10)
    elif building == 'house':
        gold_earned = random.randint(2,5)
    elif building == 'casino':
        gold_earned = random.randint(-50,50)

    request.session['gold'] += gold_earned
    request.session['moves'] += 1

    if gold_earned > 0:
        message = f'<li style="color:green">Earned {gold_earned} gold from the {building}! ({time})</li>'
    else:
        message = f'<li style="color:red">Entered a casino and lost {abs(gold_earned)} golds... Ouch.. ({time})</li>'
        
    request.session['activities'] = [message] + request.session['activities']

    max_moves = request.session.get('max_moves', 15)
    target_gold = request.session.get('target_gold', 500)

    if request.session['gold'] >= target_gold and request.session['moves'] <= max_moves:
        request.session['status'] = 'win'
    elif request.session['moves'] >= max_moves and request.session['gold'] < target_gold:
        request.session['status'] = 'lose'

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

def start_game(request):
    if request.method == 'POST':
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['moves'] = 0
        request.session['status'] = None
        request.session['max_moves'] = int(request.POST['max_moves'])
        request.session['target_gold'] = int(request.POST['target_gold'])
    return redirect('/')