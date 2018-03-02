def add(x=input("Please enter the first number"),y=input("Please enter the second number"),z=input("Please enter the third number")):
	print x,'+',y,'+',z
	return x+y+z
def main():
	print"main starts..."
	x=10
	y=20
	z=30
	print "x is base"
	print add(x,y,z)
	print add(x,y)
	print add(x)
	print "y is base"
	print add(x,y,z)
	print add(y,z)
	print add(y)
	print "z is base"
	print add(x,y,z)
	print add(x,z)
	print add(z)
	print"entered values"
	print add()
main() 