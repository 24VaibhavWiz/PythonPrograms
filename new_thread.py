from thread import start_new_thread
from time import sleep
def test():
	while 1:
		print "THREAD 1"
		sleep(1)
def demo():
	while 1:
		print "THREAD 2"
		sleep(1)
def main_thread():
	while 1:
		print "main thread"
		sleep(1)
def main():
	start_new_thread(test,())
	start_new_thread(demo,())
	main_thread()
main()