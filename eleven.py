from datetime import date

dates = int(input("Enter Your DOB: "))
my_date = date(dates)


print(my_date.strftime("%Y-%m-%d"))



