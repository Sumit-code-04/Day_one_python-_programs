#Average of 5 Numbers program

# inputs

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))
num4 = float(input("Enter the 4th number: "))
num5 = float(input("Enter the 5th number: "))
total = float(num1 + num2 + num3 + num4 + num5)

print("\n===============Result=================")
print(f"{num1} + {num2} + {num3} +{num4}  + {num5} = {round(total,2)}")
average = total / 5

print(f"\nThe Average is:{round(average,2)}")