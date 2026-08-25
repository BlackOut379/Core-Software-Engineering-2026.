def accesscontrol() :
	age = int(input("Enter the age: "))
	has_id = input("Do you have id? ")
	
	if( age>=18 and has_id=="True"):
		print("Access : Granted")
	else:
		print("Access : Denied")
		
		
def main() :
	accesscontrol()
	
main()