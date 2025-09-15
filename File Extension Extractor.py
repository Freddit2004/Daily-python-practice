#ask the user to type a filename
filename=input("Enter the filename:")

#split the file name at the dot(.)
parts=filename.split(".")
#The extension is the last part after the last dot
extension=parts[-1]
#print the result
print("The extension of the file is:",extension)