from time import sleep
def main():
	i=0;word=''
	str=input("Please enter the string of your choice : ")
	while i<=len(str):
		if str[i]== "":
			print word
			sleep(1)
			word=''
		else:
			word=word+str[i]
		i+=1
main()