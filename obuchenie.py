import math
a = 1
b = -4
c = 3

D = b*b-4*a*c

print (D)

if D>0:
	x1 = (-b-math.sqrt(D))/(2*a)
	x2 = (-b+math.sqrt(D))/(2*a)
	print (x1)
	print (x2)
else:
	print ("корней нет")
