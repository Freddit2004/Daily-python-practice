#write a python program that returns a string that is n(non-negative integer)copies of a given string
def stringCopying(s, n):
    #return n copies of the string
    return s*n

#ask user for input
text = input("Enter a String:")
num = int(input("Enter number of copies(non-negative integer):"))

#show result
print("Result:",stringCopying(text, num))