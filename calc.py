def cal():
    num1=int(input("Enter first number: "))
    opration= input("select any opration ")
    num2=int(input("Enter scond number: "))
    
    if opration == "+":
        res= num1 + num2
    elif opration == "-":
        res= num1 - num2
    elif opration == "*":
        res= num1 * num2
    elif opration == "/":
        res= num1 / num2
    elif opration == "**":
        res= (num1 ** num2)
    print (f"the result = {res}")
    

while True:
    cal() 
