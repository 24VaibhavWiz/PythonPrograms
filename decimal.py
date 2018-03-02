def main():
	dec=0;base=1;
	bin=input("Please enter binary number of your choice")
	while bin!=0:
		last =bin%10
		dec=dec+last*base
		base=base*2
		bin/=10
	print "The decimal form of the give bianry form is ",dec
main()