def main():
	fact=1
	no=input("Please enter the number :")
	while no!=1:
		fact=fact*no
		no=no-1
	print "The factorial of the number is ",fact
main()