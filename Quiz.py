print("Welcome to my Computer Quiz!")
import time
time.sleep(1.5)
playing = input("Do you want to play my game?? \n ")

if playing.lower() != "yes":
    quit()
import time
time.sleep(0.5)

print("Okay! Let's play!")
score = 0
import time
time.sleep(0.9)

answer = input("What does CPU Stand for? \n")
if answer.lower() == "central processing unit":
    print('Correct! \n Great job! Hope you get the next one!')
    score+= 1
else:
    print("Incorrect. Darn diggedy, Hope you get the next one!")

import time
time.sleep(3)

answer = input("What does GPU Stand for? \n")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect \n Don't forget to Check your Spelling.")

import time
time.sleep(2.6)

answer = input("What does RAM Stand for? \n")
if answer.lower() == "random access memory":
    print('Correct! \n This is an easy one For for Muhammad, Not the spelling tho.')
    score += 1
else:
    print("Incorrect. \n I sure do hope you know the next one!")

import time
time.sleep(4)

answer = input("What does PSU Stand for? \n")
if answer.lower() == "power supply":
    print('Correct! GREAT job!')
    score += 1
else:
    print("Incorrect. \n The letter U in PSU is very misleading to me.")

import time
time.sleep(2)
print("You got " + str(score) + "/4 Questions Correct!")

print("You got " + str((score / 4) * 100) + "%.")
print("I hope this was fun, and I hope I'll get too see " "you Next time, \n   Goodbye!!")
print("\n" * 14)  #like 5 minutes trying to Use the Multiply or * to work
print("Coded by Muhammad \n Idea by TWT")

