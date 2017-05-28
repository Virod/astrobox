
g = 0 
i = 0
while i < 100:	
	i = i + 1
	if i%7 == 0 and i%3 == 0:
		print (i)
		print ("делится на 7 и на 3")
		g = g + 1
print (g)