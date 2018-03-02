def main():
	no=input("Please enter the number :")
	temp=no
	f=1
	sum=0
	while no>0:
		last=no%10
		while last >0:
			f=f*last
			last-=1
			sum=sum+f
			no/=10
	if temp == f:
		print "I am strong"
	else:
		print "I am not strong"
main()