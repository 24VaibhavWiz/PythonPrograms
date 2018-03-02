def full(stack,sp):
	if sp==len(stack)-1:
		return 1
	else: 
		return 0
		
def push(stack,sp):
	if full(stack,sp):
		print "stack is full"
	else: 
		data =input("Enter the number")
		sp+=1
		stack[sp]=data
	return sp
def empty(stack,sp):
	if sp==-1:
		return 1
	else: 
		return 0
def pop(stack,sp):
	if empty(stack,sp):
		print "empty stack"
	else:
		stack[sp]=0
		sp-=1
	return sp
def traverse(stack,sp):
	while sp>=0:
		print stack[sp]
		sp-=1
def main():
	stack=[0,0,0,0,0,0]
	sp=-1
	while 1:
		print "1: push"
		print "2: pop"
		print "3: exit"
		ch=input("Please enter your choice")
		if ch==1:
			push(stack,sp)
			traverse(stack,sp)
		elif ch==2:
			pop(stack,sp)
			traverse(stack,sp)
		elif ch==3:
			break
		else:
			print("invalid choice")
main()