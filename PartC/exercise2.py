# ATM simulator
starting_balance: float = 1000
correct_pin: int = 1234
user_balance: float = 0

user_pin: int = int(input("Please enter a pin (4-digits): "))
if user_pin == correct_pin:
    user_action: str = input("Would you like to deposit, withdraw or deposit? ").lower()

    if user_action == "balance":
        print(f"Here is the balance: {starting_balance}")

    elif user_action == "withdraw":
        withdraw_amount: float = float(input("Enter the amount you would like to withdraw: "))

        if starting_balance - withdraw_amount >= 0:
            starting_balance -= withdraw_amount
            print(f"£{withdraw_amount} withdrawn.")
        else:
            print("The ATM does not have enough money to complete your request.")

    elif user_action == "deposit":
        keep_depositing: bool = True
        while keep_depositing:
            user_deposit: float = float(input("How much would you like to deposit? "))

            if user_deposit > 0:
                user_balance += user_deposit
                print("Deposit successful, your balance is now £", user_deposit)
            elif user_deposit == 0:
                print("You cannot deposit nothing.")
            else:
                print("You cannot take money out of the ATM with deposit, please you withdraw instead.")

            user_continue: str = input("Would you like to continue depositing (yes/no)? ").lower()
            if user_continue == "no":
                keep_depositing = False

    else:
        print("Invalid menu choice, please start over")