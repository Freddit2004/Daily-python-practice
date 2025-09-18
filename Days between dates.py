from datetime import date

#define the two dates
date1 = date(2014, 7 ,2)
date2 = date(2015, 7, 11)

#subtract the dates -> gives a timedelta object
delta = date2 - date1

#print the difference in days
print(f"{delta.days}days")
