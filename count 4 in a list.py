#write  a program to count the number 4 in a list
def countFours(num):
    return  num.count(4)

num=[1,4,5.4,5,5,55,5,5544,7,8,4,44,4,5,5,5,554]
print("Number of 4's in the list:",countFours(num))