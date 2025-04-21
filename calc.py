import math


def cal():
    num1=int(input("Enter first number: "))
    operation= input("Select an operation (+, -, *, /, **, !, |, or, and, xor):")
    

    if operation =="!":
        res = 1
        for i in range(1, num1 + 1):
            res *= i
        print(f"The result = {res}")

    elif operation == "|":
        def absolute_value(n):
            return -n if n < 0 else n
        res = absolute_value(num1)
        print(f"The result = {res}")

    else:
        num2=int(input("Enter second number: "))
        if operation == "+":
            res= num1 + num2
        elif operation == "-":
            res= num1 - num2
        elif operation == "*":
            res= num1 * num2
        elif operation == "/":
            res= num1 / num2
        elif operation == "**":
            res= (num1 ** num2)
        elif operation == "or":
            res = num1 | num2
        elif operation == "and":
            res = num1 & num2
        elif operation == "xor":
            res = num1 ^ num2
        else:
            print("Invalid operation.")
            return
        
        print (f"The result = {res}")
    

while True:
    cal() 
