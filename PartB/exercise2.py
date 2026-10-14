# Ask the user to enter an integer, then tell if it is positive negative or zero
# If positive determine if it's even or odd
# If it is greater than 100 print "This is a large number"
number: int = int(input("Enter an integer: "))

# Positive, Negative or Zero
if number > 0:
    print("This is a positive number")
    # Is even
    if number % 2 == 0:
        print("This is a positive number")
    else:
        print("This is an odd number")

elif number < 0:
    print("This is a negative number")
else:
    print("This is zero")
    


# Is large
if number > 100:
    print("This is a large number")