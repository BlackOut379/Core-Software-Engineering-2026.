def grade(x):
	if x>100 or x<0:
		print("Invalid Score!")
	elif x<59:
		print("Score: ",x)
		print("Classification: F")
	elif x<69:
		print("Score: ",x)
		print("Classification: D")
	elif x<79:
		print("Score: ",x)
		print("Classification: C")
	elif x<89:
		print("Score: ",x)
		print("Classification: B")
	else:
		print("Score: ",x)
		print("Classification: A")


def main():
	x = int(input(" Enter your Marks: "))
	grade(x)
	
main()