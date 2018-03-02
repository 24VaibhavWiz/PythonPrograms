from time import sleep
from thread import start_new_thread
def thread_funcation(name,ctime,stime):
	for i in range (ctime):
		print "I am ",name 
		sleep(stime)
def main_thread():
	while 1:
		print "main thread"
	
def main():
	start_new_thread(thread_funcation,('thread1',10,3))
	start_new_thread(thread_funcation,('thread2',20,3))
	main_thread()
main()
	








