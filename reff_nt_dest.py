def main():
	l=[11,22,33,44,55,66,77,88,99]
	print("main():",l,id(l))
	test(l)
	print "main():",l,id(l)
def test(l):
	print "test():",l,id(l)
	l.append(111)
	l.append(222)
	print "test():",l,id(l)
main()	