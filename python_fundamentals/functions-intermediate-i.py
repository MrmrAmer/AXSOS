import random

def randInt(min=0, max=100):
    if min > max:
        min, max = max, min
    num = round(random.random() * (max - min) + min)
    return num

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min=500, max=50))
print(randInt(max=-50))