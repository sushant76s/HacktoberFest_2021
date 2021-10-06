import string
import random

char = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():

	length = int(input("Enter password length: "))

	random.shuffle(char)
	
	pwd = []
	for i in range(length):
		pwd.append(random.choice(char))

	random.shuffle(pwd)

	print("".join(pwd))

# Call the Function
generate_password()