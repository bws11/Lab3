# Simple calculator
# Operators: Addition, subtraction, Multiplication, Division, Modulo, 
# Greater than, greater than or equal to, less than, less than or equal to

operators: list = [
    "addition", "subtraction", "multiplication", "division", "modulo", "greater than", 
    "greater than or equal to", "less than", "less than or equal to"
]

print("Welcome to a simple calulcator!")
print(f"Here are a list of the avaliable operators: {', '.join(operators)}")
operator_choice: str = input("Please enter your operator: ").lower()

if operator_choice in operators:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    if operator_choice == "addition":
        print(f"{first_number} + {second_number} = {first_number + second_number}")

    elif operator_choice == "subtraction":
        print(f"{first_number} - {second_number} = {first_number - second_number}")
        
    elif operator_choice == "multiplication":
        print(f"{first_number} * {second_number} = {first_number * second_number}")

    elif operator_choice == "division":
        if second_number != 0:
            print(f"{first_number} / {second_number} = {first_number / second_number}")
        else:
            print("Cannot divide by zero.")
    
    elif operator_choice == "modulo":
        print(f"{first_number} % {second_number} = {first_number % second_number}")

    elif operator_choice == "greater than":
        print(f"{first_number} > {second_number} = {first_number > second_number}")

    elif operator_choice == "greater than or equal to":
        print(f"{first_number} >= {second_number} = {first_number >= second_number}")

    elif operator_choice == "less than":
        print(f"{first_number} < {second_number} = {first_number < second_number}")

    elif operator_choice == "less than or equal to":
        print(f"{first_number} <= {second_number} = {first_number <= second_number}")

else:
    print("Invalid operator")