#write a python program to get n (non negative integer)copies of the first 2 characters of
#a given string.Return n copies of the the whole string if the length is less than 2
def stringCopies(s,n):
    if len(s) <2:
        part=s
    else:
        part=s[:2]#first 2 characters
        return part*n#repeat 'n' times

print(stringCopies("Python",3))
print(stringCopies("A",5))
print(stringCopies("HI",2))    