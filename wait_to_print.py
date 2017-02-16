#!/usr/bin/python
import time

list1 = ['I','want','to','print','this','at','the','rate','of','one','element','per','2','sec']

for x in range(0,len(list1)):
	print list1[x]
	time.sleep(2)
