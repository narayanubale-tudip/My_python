#!/usr/bin/python

a=raw_input("Enter list of word::")
list1=a.split()
temp=0
for x in range(0,len(list1)):
	max1=len(list1[x])
	if temp < max1:
		temp=max1
	else:
		max1=max1
print max1
	
