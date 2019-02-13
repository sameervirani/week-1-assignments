a = float(input("Enter First Number:"))
no2 = input("operand")
b = float(input("Enter Second Number"))

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def display_results(result):
    print(result)
if no2 == "+":
    display_results(add(a,b))
elif no2 == "-":
    display_results(subtract(a,b))
elif no2 == "*":
    display_results(multiply(a,b))
elif no2 == "/":
    display_results(divide(a,b))
else:
    print("Invalid input")
