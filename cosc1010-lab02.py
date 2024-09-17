# Lucas Dillon
# UWYO COSC 1010
# 9/16/2024
# Lab 02 
# Lab Section: 16
# Sources, people worked with, help given to: NA

# I checked on canvas for my lab section, I believe it is section 16 as
# that is the only section held at 6:10 to 8:00 on Mondays.

your_variable_here = "when you see this, replace it with your code"

## Section ONE

# Complete the following print statement to print out "Hello, COSC1010"
print("Hello, COSC1010")

# Assign the string above to a variable named hello_message and print that variable
hello_message = "Hello, COSC1010"
print(hello_message)

# Assign the string "cowboy joe" to a variable, and print that variable with title casing
titlevar = "cowboy joe"
print(titlevar.title())

# Complete the following f-string print message 
    # You will need to create your own variables and insert them  
    # the final message should read `The University of Wyoming was founded in 1886`

uwyo = "University of Wyoming"
date = "1886"

print(f"The {uwyo} was founded in {date}")

# Now let's do some math with variables 
    # Create two variables x and y and assign them the values 5 and 10 respectively 
    # Complete the following print statements using your variables
    #All math must be done within the braces in the f-strings

x = 5
y = 10

print(f"x + y = {x+y}")
print(f"x - y = {x-y}")
print(f"x * y = {x*y}")
print(f"x / y = {x/y}")

# String concatenation 
    # Finally we will take a look at string concatenation
    # String concatenation combines two strings together
    # It is done using the + operator
    # Create three variables:
        # first_name, which is your first name 
        # last_name, which is your last name
        # space, which is a space character 
    # Use string concatenation to print out your full name 

first_name = "Lucas"
last_name = "Dillon"
space = " "

full_name = first_name + space + last_name
print(full_name)

#Concatenation does not work between types, for example you cannot
#concatenate integers and strings.
# print(1 + ", two") would give "unsupported operand types"
# print(1 + 3) is not concatenation, but integer addition.