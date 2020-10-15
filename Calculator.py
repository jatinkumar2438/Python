i = "y"

print("")
print("Welcome, I will help you with calculations.\n")

while i == "yes" or i == "y":

    num1 = float(input("Enter First Number : "))

    op = input("Enter Operator (+ - * / ^) : ")

    num2 = float(input("Enter Second Number : "))

    print("")

    if op == "+":
        print("Result : " + str(num1 + num2))
    elif op == "*":
        print("Result : " + str(num1 * num2))
    elif op == "-":
        print("Result : " + str(num1 - num2))
    elif op == "/":
        print("Result : " + str(num1 / num2))
    elif op == "^":
        print("Result : " + str(pow(num1,num2)))
    elif op != "+" or op != "-" or op != "*" or op != "/" or op != "^":
        print("ERROR : Invalid Operator")
        print("\nUse amongst one of these:\nAddition : + \nSubstraction : - \nMultiplication : * \nDivision : /\nSquare : ^")
    else:
        print("ERROR : Unknown Error Occurred.")

    print("")

    i = input("Wanna Try That Again (Yes/No) : ").casefold()
    print("")
    
print("Thank for using our application.")
print("Follow me on Instagram   @jatinkumar2438")