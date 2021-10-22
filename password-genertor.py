import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90)) 


#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 # + ....
password = shuffle(password)

#Ouput
print(password)
