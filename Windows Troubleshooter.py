import os
import time

def Windows_Diagnostics():
    print("Looking for problems.")
    time.sleep(7)
    print("Unable to fix the problem.\n")

i = "y"

print("Windows Troubleshooter\n")

while i == "yes" or i == "y":
    print("1. Applications and Services")
    print("2. Hardware and Sound")
    print("3. Network and Internet")
    print("4. System and Security")

    print("")

    type = int(input("Choose one of the following options to troubleshoot : "))

    if type == 1 or type == 2 or type == 3 or type == 4:
        Windows_Diagnostics()
    elif type != 1 or type != 2 or type != 3 or type != 4:
        print("Sorry, Your choose options that weren't recognized.")
    else:
        print("UNKNOWN ERROR OCCURED()")

    print("")

    i = input("Wanna Try That Again? (Yes/No) : ").casefold()
    print("")
    
print("Thank for using our application.")
print("You were fooled. Sorry()")
print("Follow me on Instagram   @jatinkumar2438")