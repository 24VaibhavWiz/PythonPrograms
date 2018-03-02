def main():
	a=input("The enter the first number :")
	b=input("The enter the second number :")
	range=input("Please enter the range")
	i=0;count=0;
	print a
	print b
	while count!=range:
		c=a+b
		count +=1
		print c
		a=b
		b=c
main()