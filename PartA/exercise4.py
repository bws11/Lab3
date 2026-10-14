# Ask the user to enter a mark between 0 and 100 and give them a grade
mark: int = int(input("Enter your mark: "))

if 70 <= mark <= 100:
    print("First")
elif 60 <= mark <= 69:
    print("Upper Second")
elif 50 <= mark <= 59:
    print("Lower Second")
elif 40 <= mark <= 49:
    print("Pass")
elif 0 <= mark < 40:
    print("Fail")
else:
    print("Invalid mark")