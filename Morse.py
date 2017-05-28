dict = 	{
	"a" : "-",
	'b' : "-...", 
	'c' : "-.-.",
	'd' : "-..",
	'e' : ".",
	'f' : "..-.",
	'g' : "--.",
	'h' : "....",
	'i' : "..",
	'j' : ".---", 
	'k' : "-.-",
	'l' : "..",
	'm' : "--",
	'n' : "-.",
	'o' : "---",
	'p' : ".--.",
	'q' : "--.-",
	'r' : ".-.",
	's' : "...",
	't' : "-",
	'u' : "..-" ,
	'v' : "...-",
	'w' : ".--",
	'x' : "-..-",
	'y' : "-.--",
	'z' : "--.."
}

def dot():
  	print("ON . OFF")

def dash():
 	print("ON ... Off")

s = input("s = ")

for a in s:
	print(a)
	code = dict [a]
	# print (code)
	
	for el in code:
		 print(el)
		 if el == ".":
		 	dot()
		 else :
		 	dash()






	