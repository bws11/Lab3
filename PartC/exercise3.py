# LRRL

path: list = ['l', 'r', 'r', 'l']
alive: bool = True
index: int = 0

while alive == True and index < 4:
    user_choice = input("Which door would you like to go through (L/R)? ").lower()
    if user_choice == path[index]:
        print("Correct choice! You may contine...")
        index += 1

    else:
        print("Wrong! Game Over")
        alive = False

if alive == True:
    print("You found the exit!")

# No fail print here as it was done in the loop