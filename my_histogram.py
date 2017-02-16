#!/usr/bin/python
def histogram(x) :
    for n in x:
	times = n
        output = ''
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)
histogram([1, 2,3,4,5,6,7,8,9])
