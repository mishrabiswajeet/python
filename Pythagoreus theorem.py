import math as m
def pythagorean(a,b):
    c = (a,b,m.floor(m.sqrt(m.pow(a,2)+m.pow(b,2))))
    print(*c)
a = int(input())
b = int(input())
pythagorean(a,b)
