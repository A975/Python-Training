import math

first = "Dave"
last = "Gray"

print(type(first))
print(type(last) == str)
print(isinstance(first, str))

#Multiline  lines
multilines = '''
Hey, how are you?

I was just checking in.

                    All good ?
'''
print(multilines)

#Escaping special characters
sentence = 'I\'m back at work! \t Hey!\n\n Where\'s this at \\located?'
print(sentence)

#String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multilines.title())
print(multilines.replace("good","ok"))
print(multilines)

print(len(multilines))
multilines += "     "
multilines += "       " + multilines

print(len(multilines))


print(len(multilines.strip()))
print(len(multilines.lstrip()))
print(len(multilines.rstrip()))

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$4".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))


print("")

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])

#Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))
print(first.endswith("D"))
print(first.startswith("D"))
print(first.startswith("D"))


#Boolean data type
myvalue = True
myvalue = False
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))


#Numeric data type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#Float type 
gpa = 3.28
y = float(1.14) 
print(type(gpa))
print(round(gpa))
print(abs(gpa))

#complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a string to a number
zipcode = "100001"
zip_value = int(zipcode)
print(type(zipcode))

#Error if you attempt to cast incorrect data
zip_value = int("New York")
print(zip_value)