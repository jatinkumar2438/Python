i = "yes"
tried = 0
user = 0

import random
import time

print("")
print("Guess a correct number between 0 and 10\n")
time.sleep(1)

while i == "yes" or i == "y":
    random_no = random.randint(0,9)
    while tried<3:
        user = int(input("Guess the no : "))
        if user<0 or user >9:
            print(str(user)+" is not in range. Try again.")
        elif  user != random_no:
            tried = tried + 1
            if tried <3:
                print("Oh! Wrong Number. Try Again")
            elif tried == 3:
                print("You didn't guess the correct number. ["+str(random_no)+"]")
        elif  user == random_no:
            print("You guessed the number correct. ["+str(random_no)+"]")
            tried = 3

    print("")
    i = input("Wanna Play That Again (Yes/No) : ").casefold()
    tried = 0
    print("")
    
print("Thank for using our application.")
print("Follow me on Instagram   @jatinkumar2438")