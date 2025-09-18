#aask the user for a function name
func_name=input("Enter a built-in function name(e.g.,abs,len,max):")
#use eval() to get the actual function object from the name
func=eval(func_name)
#print its documentation
print(func.__doc__)
