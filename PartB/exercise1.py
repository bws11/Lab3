# Ask the user for their age and height in cm
age: int = int(input("How old are you? "))
height: int = int(input("How tall are you? "))

if age < 12:
    print("You are too young for this ride.")
elif height >= 140:
    print("You can ride!")
else:
    print("You do not meet the height requirement.")