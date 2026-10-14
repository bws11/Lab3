# Make a simple number guessing game
secret_number: int = 7

answered_correctly: bool = False

while answered_correctly == False:
    user_answer = int(input("Enter a number: "))
    
    if user_answer == secret_number:
        print("Correct")
        answered_correctly = True
    else:
        print("Wrong! Try again")
