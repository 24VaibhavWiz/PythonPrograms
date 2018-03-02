from os import *
from time import sleep
def main():
	k=open("data.txt","r")
	pid=k.read
	k.close()
	pid = int(pid)
	c=0
	while 1:
		sleep(1)
		c+=1
		if c==5:
			kill(pid,19)
		elif c==10:
			kill(pid,18)
			c=0
main()