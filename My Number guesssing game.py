import random
print("NUMBER GUESSING GAME.")
print("You guess a number between upper bound and lower bound")
#enter the lower bound
low=int(input("Enter the Lower Bound:"))
#enter the upper bound
high=int(input("Enter the Upper Bound:"))

print(f'You are going to guess a number from {low} to {high}.')
num=random.randint(low,high)
#this is will generate the number that you are supposed to guess
chances=5
#maximum guesses are 5
GuessCO=0#this is the guess counter
while GuessCO<chances:
    GuessCO+=1
    guess=int(input("Enter the number of your choice:"))
    if guess == num:
        print("Correct!! You have won the game.")
    elif GuessCO == chances and guess!=num:
        print("You have completed your chances.START AGAIN!!")
    elif guess> num:
        print("Too high!!TRY AGAIN")
    elif guess < num:
        print("Too low!!TRY AGAIN")


