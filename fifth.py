# area of circle program
import math
PI = math.pi
radius = float(input("Enter the Radius of Circle:"))

area = PI * pow(radius,2)

print("\n==========Result===========")
print(f"The are of Circle is: {round(area,2)}cm²")