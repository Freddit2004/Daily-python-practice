import calendar

#ask the user for year and month
year=int(input("Enter year:"))
month=int(input("Enter month:"))

print("\nHere is the calendar:\n")
print(calendar.month(year, month))