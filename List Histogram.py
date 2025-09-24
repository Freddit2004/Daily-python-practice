#write a python program to create a histogram fro a given list of integers
#showing bars(using*) for each number in the list
def histogram(numbers):
    for n in numbers:#loop through each number in the list
        print('*'*n)#print n stars to represent the number

#example
histogram([2,3,4,5,67,54])        
