while True:
    height = int(input("height: "))
    if(height > 0):
        break
for i in range(height):
    if(i == 0):
        print("* "*(height))
    elif(i> 0 and i <= height-2):
        print("* ", end="")
        print("  "*(height-2), end="")
        print("* ")
    else:
        print("* "*height, end="")
    