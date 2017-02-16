#!/usr/bin/python
import random
dict1={1123456:"Nikhil",6546565:"Ankit",1316654:"Digres",46464464:"Aditya",4646464:"Yadnya"}
def lucky() :
	win=random.sample(dict1,1)
	print "Winner is ::\t", dict1[win[0]]
lucky()

