#!/usr/bin/python
import random,string
a=string.digits+string.letters+string.punctuation
password1=""
final=""
p=random.sample(a,8)
for x in range(0,len(p)):
		password1=password1+p[x]
print "Password generated::\t",password1

for x in range(0,len(p)):
	first=password1[x]
	for x in range(0,len(a)):
		if first==a[x]:
			final=final+first
			print final
			break
		else:
			pass
print "password:: ",final	



	
 



