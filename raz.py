import RPi.GPIO as GPIO    

import time        
PIN = 7
# PIN = 4

GPIO.setmode(GPIO.BOARD)   
# GPIO.setmode(GPIO.BCM)   

GPIO.setup(PIN, GPIO.OUT)    

while True:                
	GPIO.output(PIN, 1)      
	print ("ON")
	time.sleep(1)          
	GPIO.output(PIN, 0)
	print("OFF")      
	time.sleep(1)         