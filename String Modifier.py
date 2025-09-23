#write a python program to get a newl generated string from a given string where "Is"
#has been added to the front.Return the string unchanged if the given string already begins"Is".
def addprefixIs(s):
    #check if the string already starts with"Is"
    if s.startswith("Is"):
        return s
    else:
        return "Is" + s
    
text=input("Enter a string:") 
print("Result:",addprefixIs(text))
