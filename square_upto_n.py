#!/usr/bin/python
dict1={}
n= input("Enter value of n::")
list1=[]
for x in range(1,n+1):
	list1.append(x)
list2=[]
for x in list1:
	list2.append(x*x)

for x in range(1,n+1):
	dict1[x]=list2[x-1]

print dict1
