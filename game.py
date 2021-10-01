import random
import time
print("\t\t***Welcome to the Game***")
time.sleep(1)
choice=["Rock", "Paper", "Scissor"]
c_score = 0
u_score = 0
print(f"\tEnter Number for: \n Rock    -> 1\n Paper   -> 2\n Scissor -> 3\n")
t_round = int(input("Enter no of rounds want to play: "))

for i in range(t_round):
    time.sleep(.5)
    print("\n\t\t*** Your Turn ***")
    time.sleep(1)
    u_choice = int(input("\tEnter Your Choice: "))
    time.sleep(1.5)
    print("\tYour Choice  : ", choice[u_choice - 1])
    time.sleep(1)

    print("\n\t\t *** System's turn ***")
    c_choice = random.randint(0, 2)
    time.sleep(1)
    print("\tSystem choice: ", choice[c_choice])

    if (choice[u_choice - 1] == choice[c_choice]):
        c_score += 0
        u_score += 0
    elif(choice[u_choice - 1] == choice[0] and choice[c_choice] == choice[1]):
        c_score += 1
    elif(choice[u_choice - 1] == choice[1] and choice[c_choice] == choice[2]):
        c_score += 1
    elif(choice[u_choice - 1] == choice[2] and choice[c_choice] == choice[0]):
        c_score += 1
    else:
        u_score += 1


if(c_score > u_score):
    print("\t\t*** Bad Luck! System Won *** ")
    time.sleep(2)
elif(c_score < u_score):
    print("\t\t *** Hurry! You Won *** ")
    time.sleep(2)
else:
    print("\t\t***Game Tied***")
    time.sleep(1.5)
print("\tSystem score: ", c_score)
print("\tYour Score  : ", u_score)