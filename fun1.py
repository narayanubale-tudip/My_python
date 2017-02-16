#!/usr/bin/python

def choice():
	print "1.Calculate SI\n2.Calculate CI\n"
	ch=input("Enter Choice::\t")
	if ch==1:
		calculate(p,n,r)
	else:
		calculate1(p,n,r)
		

def calculate(p,n,r):
	result= (p*n*r)/100
	print "Simple Interest::\t", result

def calculate1(p,n,r):
	t=input("Time::\t")
	result= p*(1+ r/n)**(n*t)
	print "Compound Interest::\t", result

p=input("Enter Principle::\t")
n=input("Enter Period::\t")
r=input("Enter Rate::\t")
choice()


