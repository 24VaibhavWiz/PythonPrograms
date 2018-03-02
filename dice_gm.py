import random
def main():
	no=input("Please enter the number of your choice to roll the dice")
	bet=input("Please enter the bet you want for the game")
	ran=random.randint(1,7)
	count=1
	while count<=2:
		if(ran>no):
			print("your guess is little less.....")
			print "you lose" , bet
			count+=1
	                no=input("Please enter the number of your choice to roll the dice")
		elif(ran<no):
			print("your guess is little larger.....")
			print "you lose" , bet
			count+=1
      	                no=input("Please enter the number of your choice to roll the dice")
		elif(ran==no):
			print("your guess is right.....")
			count=3
main()