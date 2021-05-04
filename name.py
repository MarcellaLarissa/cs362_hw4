def fullName(fName, lName):
    name = fName + " " + lName
    return name
    
    
    
    
#driver code
fName = input("Please enter first name\n")
lName = input("Please enter last name\n")

name = fullName(fName, lName)

print(name)
