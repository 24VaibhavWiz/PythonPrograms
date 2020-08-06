import json
import re

d = {} 
while True:
	print("\nOperations") 
	print("\n1.Add Contacts\n2.List all the contacts\n3.List the phone number of the given email_id\n4.Update the phone number\n5.Reopen the Saved Data\n6.Exit") 
  
	ch = int(input("Enter choice:")) 

	if(ch == 1):
		k = raw_input("Enter Email id: ")
	    	if not re.match(r"[^@]+@[^@]+\.[^@]+", k):
			raise Exception("Sorry, invalid email id")
	
		v = raw_input("Enter Phone no.: ")
		
		if((len(v) == 10)and(v.isdigit())):
			d.update({k:v})
		c
	elif(ch == 2): 
		print("\n") 
		print("\nList of Contacts\n") 
		print(d) 

	elif(ch == 3): 
		g = raw_input("Enter email id : ") 
		if not re.match(r"[^@]+@[^@]+\.[^@]+", g):
			raise Exception("Sorry, invalid email id")
		print(d.get(g))

	elif(ch == 4): 
		g = raw_input("Enter email id : ") 
		if not re.match(r"[^@]+@[^@]+\.[^@]+", g):
			raise Exception("Sorry, invalid email id")
		print(d.get(g))
		n = raw_input("Enter new number : ") 
		if((len(n) == 10)and(n.isdigit())):
			d1 = {g: n}
			d.update(d1)
		else:
			raise Exception("Sorry, invalid phone number")
  
			
	elif(ch == 5):
	#reopen the saved data 
		with open('data.json','r') as f:
				data = json.load(f)

	else:
		with open('data.json', 'w') as f:
    			json.dump(d, f)
		break
