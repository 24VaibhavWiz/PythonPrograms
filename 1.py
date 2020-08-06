#Indian Phone Numbers only
import json
import re
d={}

try:
	with open('Data.json','r') as f:
		d = json.load(f)
except:
	print("\nFile not found\n")
	print("\n*****You can only Add Contacts*****")	

 
while True:
	print("\nOperations") 
	print("\n1.Add Contacts\n2.List all the contacts\n3.List the phone number of the given email_id\n4.Update the phone number\n5.Exit") 
  
	ch = int(input("\nEnter your choice:")) 

	if(ch == 1):

		k = raw_input("\nEnter Email ID: ")
	    	if not re.match(r"[^@]+@[^@]+\.[^@]+", k):
			raise Exception("\nSorry, Invalid Email ID")
		
		v = raw_input("\nEnter Phone Number.: ")
		if not re.match(r"^((\+){1}91){1}[1-9]{1}[0-9]{9}$", v):
			raise Exception("\nSorry, Invalid Phone Number")
		else:
			d.update({k:v})

	elif(ch == 2): 

		print("\n") 
		print("\nList of Contacts\n") 
		print(d) 
	
	elif(ch == 3): 

		g = raw_input("\nEnter Email ID: ") 
		if not re.match(r"[^@]+@[^@]+\.[^@]+", g):
			raise Exception("\nSorry, Invalid Email ID")
		print(d.get(g))

	elif(ch == 4): 

		g = raw_input("\nEnter Email ID : ") 
		if not re.match(r"[^@]+@[^@]+\.[^@]+", g):
			raise Exception("\nSorry, Invalid Email ID")
		print(d.get(g))

		n = raw_input("\nEnter new the Number : ") 
		if not re.match(r"^((\+){1}91){1}[1-9]{1}[0-9]{9}$", n):
			raise Exception("\nSorry, Invalid Phone Number")
		else:
			d1 = {g: n}
			d.update(d1)

	else:

		with open('Data.json', 'w') as f:
    			json.dump(d, f)
		
		break
