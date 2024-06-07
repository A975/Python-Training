class JustNotCoolError(Exception):
    
    pass

x = 2

try:

    if not type(x) is str:
        
        raise TypeError("Only strings are allowed.")
        # x = int(input("Please enter a number: "))
        
except SyntaxError:
    
    print("This is raised when the interpreter encounters a syntax error in the code, such as a misspelled colon , or an unbalanced parenthesis")
    
except ZeroDivisionError:
    
    print('please do not divide by zero.')

except TypeError:

    print("This exception is raised when an operation or function is applied to an object of the wrong type such as adding a string to an interger")
    
except NameError:
    
    print("This exceis not option is raised when a variable or function name is not found in the current scope")

except IndexError:

    print("This exception is raised when an index is out of range for a list tuple or other sequence types")

except KeyError:

    print("This exception is raised when a key is not found in dictionary")

except ValueError:

    print("This exception is raised when a function or method is called with an invalid argument or input such as trying to convert string to an integer when the string does not represent a valid interger")

except AttributeError:

    print("This exception is raised when an attribute or method is not found on an object, such as tying to access a non-existent attribute of a class instance")
    
finally:
    
    print("I'm going to print with or without an error.")
