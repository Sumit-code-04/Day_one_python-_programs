# Simple Interest Calculator

P = float(input("Enter the Principle Amount(borrowed/invested):₹ "))
R = float(input("Enter the Rate of Interest per year(e.g. use 5 for 5%): "))
T = float(input("Time Period(e.g 1yr,2yrs..): "))

SI = (P * R * T )/ 100
print("============Result===========")
print(f"Total is: ₹{SI}")