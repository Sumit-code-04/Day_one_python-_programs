num1 = float(input("Enter The first Number:"))
num2 = float(input("Ente The Second Number:"))

print(f"num1:{num1} \nnum2:{num2}")

#  Method 1
temp = num1
num1 = num2
num2 = temp
print("========Method 1:======= \n")
print(f"Swapped number is:\nnum1:{num1} \nnum2:{num2}")

#  Method 2
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("========Method 2:======= \n")
print(f"Again Swapped number is:\nnum1:{num1} \nnum2:{num2}")

#  Method 3
num1,num2 = num2,num1
print("========Method 3:======= \n")
print(f"Again Swapped number is:\nnum1:{num1} \nnum2:{num2}")
