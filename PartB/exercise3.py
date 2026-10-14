# Simple login system
correct_username: str = "student"
correct_password: str = "python123"

user_username: str = input("Enter your username: ")
user_password: str = input("Enter your password: ")

# Old
# if (user_username == correct_username) and (user_password == correct_password):
#     print("Logged in successfully")
# else:
#     print("Incorrect username or password")

# Modified task
if (user_username == correct_username) and (user_password == correct_password):
    print("Logged in successfully")

    user_age: int = int(input("Enter your age: "))
    if user_age >= 18:
        print("Access granted")
    else:
        print("You must be atleast 18")

elif (user_username == correct_username) and (not (user_password == correct_password)):
    print("Username recognised, but password is incorrect")