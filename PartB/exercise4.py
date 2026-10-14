# Ask the user to enter the total amount of their shopping
# < £50 no discount
# 50 <= x < 100 10% off
# 100 <= x 20% off

amount: int = int(input("How much was your shopping? "))
discount: int = 1

if amount < 50:
    print("Sorry, you get no discount.")

else:
    if amount < 100:
        print("You get 10% off")
        discount = 0.1
    else:
        print("You get 20% off")
        discount = 0.2

    # Only do discount logic if needed
    money_off: float = amount * discount
    print(f"Discount: £{money_off}")
    print(f"Final amount: £{amount - money_off}")