#!/usr/bin/python
import random
no = 1
while no <= 4:
	print " this is your",no,"turn"
	a = input(" Enter Your Guess :")
	num = random.randint(1,4)
	print "Random Number is",num
	if a == num :
		print ("***** Your no. is match you won ****** ")
		print " you won in your",no,"guess"
		break;
	else :
		print (":( better luck next time :( ")
		print ("You can try once more")
	no = no +1
print "Thank you for your support"


