def main():
	x=10
	print "main():",x,id(x)
	x=test(x)
	print "main():",x,id(x)
def test(x):
	print "test():",x,id(x)
	x+=1
	print "test()",x,id(x)
	return x
main()