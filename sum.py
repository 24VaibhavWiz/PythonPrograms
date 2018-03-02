def main():
	sum=0
	no=input("Please enter the number : ")
	while no>0:
		last=n%10
		sum=sum+last
		no/=10
	print "The sum is ",sum
main()