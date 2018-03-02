from os import *
from time import sleep
def main():
	k=fork()
	if k==0:
		while 1:
			print"hello",		
	else:
		c=0
		while 1:
			sleep(1)
			c+=1
			if c==5:
				kill(k,19)
			if c==10:
				kill(k,18)
				c=0
main()				