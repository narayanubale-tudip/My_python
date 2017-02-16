#!/usr/bin/python

a = {1:"MOUSE",2:"KEYBOARD",3:"CPU",4:"MONITOR"}
m= {1:100,2:500,3:2000,4:1000}
stock={1:10,2:10,3:10,4:10}
w=stock.values()
y=a.keys()
j=a.values()
z=m.values()
cart=[]

def purchase() :
	b1=input("Select ITEM::\t")
	item=input("Number of item::\t")
	if w[b1-1]-item < 0:
		print "Much Stock nt available!!"
	else:
		for x in range(0,item):
			cart.append(b1)
		w[b1-1]=w[b1-1]-item
		print "Item Purchased:: {} {}".format(item,a[b1])

def delete(e) :
	cart.remove(e)
	w[e-1]=w[e-1]+1

def view() :
	for x in range(0,len(y)):
 		print y[x],"\t",j[x],"\t",z[x],"\t",w[x]

def calculate() :
	bill=0
	for x in range(0,len(cart)):
		q=cart[x]
		bill=bill + m[q]
	print bill

def check() :
	u=input("Enter Item::\n")
	v=w[u-1]
	if v!=0:
		print "Available::\t",w[u-1]
	else:
		print "Not available!!"


while 1:
	print "1.ADD To CART 2.DELETE ITEM 3.DISPLAY CART 5.CLEAR CART 6.EXIT 7.VIEW ITEMS 8.Calculate Bill\n9.CKECK AVAILABILITY\n"
	b=input("Enter Choice::\t")
	while 1:
		if b==1:
			purchase()
			break
		elif b==2:
			e=input("Select ITEM::\t")
			delete(e)
			break
		elif b==3:
			print cart
			break
		
		elif b==5:
			cart=[]
			break
		elif b==6:
			exit()
		elif b==7:
			view()
			break
		elif b==8:
			calculate()
			break
		elif b==9:
			check()
			break
		else:
			print "Enter Valid Choice!"

