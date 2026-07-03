#simple calculator
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

operator = input("Select an operation which you want to perform (+ , - , * , /): ")

if operator == "+":
    result = num1 + num2
    print("\n============Result=============")
    print(f"The addition is: {result}")
elif operator == "-":
    result = num1 - num2
    print("\n============Result=============")
    print(f"The Subtraction is: {result}")
elif operator == "*":
    result = num1 * num2
    print("\n============Result=============")
    print(f"The Multiplication is: {result}")
elif operator == "/":
    result = num1 / num2
    print("\n============Result=============")
    print(f"The Division is: {result}")
else:
    print(f"{operator}Invalid Operator")
