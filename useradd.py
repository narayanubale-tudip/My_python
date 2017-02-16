#!/usr/bin/python
import os
import sys
import crypt
name = raw_input ("Enter a name :")
useradd = raw_input("Enter User name :")
passwd	= raw_input("Enter Password :")
def createuser (name,useradd,passwd):
	epass = crypt.crypt(passwd,"22")
	return os.system(" useradd -p"+epass+ "-s" +"/bin/bash"+"-d"+"/home/"+useradd+"-m"+"-c \""+name+"\"" +useradd) 
createuser(name,useradd,passwd)

