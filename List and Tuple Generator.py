#ask the user to type in numbers separated by commas
numbers=input("Enter a sequence of comma-separated numbers:")
#we use.split(",")to break it into pieces wherever there is a comma
list_numbers=numbers.split(",")
#convert the list into a tuple
tuple_numbers=tuple(list_numbers)
print("List:",list_numbers)
print("Tuple:",tuple_numbers)