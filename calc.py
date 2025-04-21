import math


def cal():
    num1=int(input("Enter first number: "))
    operation= input("Select an operation (+, -, *, /, **, ! , |):")
    

    if operation =="!":
        res = math.factorial(num1)
        print (f"the result = {res}")
    elif operation == "|":
        res = abs(num1)
        print(f"The result = {res}")
    else:
        num2=int(input("Enter scond number: "))
        if operation == "+":
            res= num1 + num2
        elif operation == "-":
            res= num1 - num2
        elif operation == "*":
            res= num1 * num2
        elif operation == "/ ":
            res= num1 / num2
        elif operation == "**":
            res= (num1 ** num2)
        else:
            print("Invalid operation.")
            return
        
        print (f"the result = {res}")
    

while True:
    cal() 
