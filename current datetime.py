import datetime
#python doesn't magically know time it borrows from this module"datetime"

now=datetime.datetime.now()
#now is a variable where we store the current date and time

print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
#strftime=string format time
#"please convert this complicated date object into a human readable string"