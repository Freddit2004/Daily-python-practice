#write a python program that determines whether a given number(accepted by
#the user)is even or odd, and prints a appropriate message to the user
def number_checker(n):
    if n%2==0:
        print("This is an even number.")
    else:
        print("This is an odd number.")

n=int(input("Enter a number;")) 
print("Output:", number_checker(n))           