def main():
	no=input("Please enter the number :")
	dig=0
	while no!=0:
		last =n%10
		dig+=1
		n/=10
	print "The digits are ",dig
main()