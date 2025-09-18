#write a python program to calculate the sum of three given numbers.
#if the values are equal, return three times their sum
def sum(a,b,c):
    #if the three numbers are equal
    if a==b==c:
        return 3*(a+b+c)
    else:
        return a+b+c
    
a=int(input("Enter first number:"))
b=int(input("Enter the second number:")) 
c=int(input("Enter the third number:"))   

#show the result
print("Result:", sum(a,b,c))