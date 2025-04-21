import math


def cal():
    num1=int(input("Enter first number: "))
    opration= input("Select an operation (+, -, *, /, **, !):")
    

    if opration =="!":
        res = math.factorial(num1)
        print (f"the result = {res}")
    else:
        num2=int(input("Enter scond number: "))
        if opration == "+":
            res= num1 + num2
        elif opration == "-":
            res= num1 - num2
        elif opration == "*":
            res= num1 * num2
        elif opration == "/ ":
            res= num1 / num2
        elif opration == "**":
            res= (num1 ** num2)
        else:
            print("Invalid operation.")
            return
        
        print (f"the result = {res}")
    

while True:
    cal() 
