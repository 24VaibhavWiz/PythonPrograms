from thread import start_new_thread
from time import sleep
flag=[]
def test(name):
	while 1:
		if [name,0]in flag :
			flag.pop(flag.index([name,0]))	
			print flag
			sleep(1)
			break
		print "I am thread",name
		sleep(1)
def main():
	global flag
	while 1:
		data=raw_input("")
		if data.split()[0]=="start":	
			flag.append([data.split()[1],1])	
			print flag
		 	sleep(2)
			start_new_thread(test,(data.split()[1]))
		elif data.split()[0]=="stop":
			index=flag.index([data.split()[1]])
			flag[index][1]=0
main()