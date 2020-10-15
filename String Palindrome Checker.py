
x = "y"
print()
print("Hello, I will help you checking whether a Text is Palindrome or not!\n")


while x == "yes" or x == "y":
    
    text = input("Please enter your Text: ").casefold()
    l = len(text)
    i = l
    rev = ""
    
    while i >0:
        rev += text[i-1]
        i = i-1

    if rev == text:
        print(text + " is a Palindrome.") 
    elif rev != text:
        print(text + " is not a Palindrome.")
    else:
        print("ERROR:")

    print("")

    x = input("Restart this application (Yes/No) : ").casefold()
    print("")
    
print("Thank for using our application.")
print("Follow me on Instagram  @jatinkumar2438")
