#write a python program to test whether a umber is within 100 of 1000 or 2000
def nearNumber(n):

    return (abs(1000-n) <= 100) or (abs(2000) <=100)
n=int(input("Enter a number:"))
#display the result
if nearNumber(n):
    print("Yes,", n, "is within 100 0f 1000 or 2000.")
else:
    print("No,", n, "is not within 100 of 1000 or 2000.")    