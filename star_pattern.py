a=int(input("ENTER THE NUMBER OF ROWS:\n"))
b=int(input("ENTER\n0:FOR REVERSE STAR PATTERN\n1:FOR STAR PATTERN5\n"))
n=bool(b)
print("\n")

if n==True:
	for i in range(0,a+1):
			print("*"*int(i))
	
if n==False:
	for i in range(a,0,-1):
			print("*"*int(i))
   
   
"""
OUTPUT:

ENTER THE NUMBER OF ROWS:
5
ENTER
0:FOR REVERSE STAR PATTERN
1:FOR STAR PATTERN        
1

*    
**   
***  
**** 
*****

"""
