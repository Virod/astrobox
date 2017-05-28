import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b*b-4*a*c

def calc(x):
	return a*x*x + b*x + c

def mul2(x):
	return x*2


print(calc(7))

if d < 0:
	print ("D - меньше 0")
else:
	print ("D", d)
	x1 = (-b - math.sqrt(d)) /(a*2)
	x2 = (-b + math.sqrt(d)) /(a*2)
	print ("x1", x1)
	print ("x2", x2)
	assert calc(x1) == 0
	assert calc(x2) == 0