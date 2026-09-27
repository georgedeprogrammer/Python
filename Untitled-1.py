Username = int(input("Enter your username: "))
Password= int(input("Enter password: "))
if Username == George and Password == 12345:
    print("Access granted")
else:
    print("Not granted")
# age checker
from datetime import datetime
Y.O.B = int(input("Enter date of birth:"))
current_year = datetime.now().year
age = current_yaer - Y.O.B

#simple calc
def add(x,y):
    return x+y
def division(x,y):
    return x/y
def multiply(x,y):
    return x*y
def subtract(x,y):
    return x-y
print("Selectd opration")
num1 = int(input("Enter first number of operation:"))
num2 = int(input("Enter second number of operation"))
operation = input("Enter operation(+,/,-,*)")
if operation == "+":
    print(add(num1,num2))
elif operation == "/":
    print(division(num1,num2))
elif operation == "*":
    print(multiply(num1,num2))
elif operation == "-":
    print(subtract(num1,num2))
else:
    print("Syntax error")
            