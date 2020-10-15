
x = "y"
print()
print("Hello, I will help you checking whether a Number is Palindrome or not!\n")


while x == "yes" or x == "y":

    no = int(input("Please enter your Number: "))
    rev = 0
    temp = no

    while round(temp) != 0:
        rev = round((rev*10) + (temp%10))
        temp = temp/10

    if rev == no:
        print(str(no) + " is a Palindrome.") 
    elif rev != no:
        print(str(no) + " is not a Palindrome.")
        print(rev)
    else:
        print("ERROR:")

    print("")

    x = input("Restart this application (Yes/No) : ").casefold()
    print("")
    
print("Thank for using our application.")
print("Follow me on Instagram  @jatinkumar2438")
