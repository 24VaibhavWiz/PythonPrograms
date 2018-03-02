def main():
	no=input("Please enter the number :")
	rev=0
	while no>10:
		last =n%10
		rev=rev*10+last
		n/=10
	print "The reversed number is ",rev
	if rev == no:
		print "yes it is palindrome"
	else:
		print "no it is not pallindrome"
main()