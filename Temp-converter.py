

unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ").upper()
temp = float(input("Enter the Temperature: "))

if unit == "C":
    temp = round((9*temp) / 5 + 32, 1)
    print(f"The temperature in fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is: {temp}°C")
else:
    print(f"{unit} is invalid unit of measurement")
