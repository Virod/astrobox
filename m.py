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


def element(e):
	 print(e)
	 if e == ".":
	 	dot()
	 else:
	 	dash()

def letter(ch):
	print(ch)
	code = dict[ch]
	# print (code)
	
	for el in code:
		element(el)

s = input("s = ")
for a in s:
	letter(a)




	