# Ask for their age, order total (£), account status (y/n), valid discount code

age: int = int(input("Enter your age: "))
order_total: float = float(input("Enter your order total (£): "))
account_status: str = input("Enter the status of your account (yes/no): ").lower()
has_discount: str = input("Do you have a valid discount code (yes/no)? ").lower()

if account_status == "yes":

    if order_total < 0:
        print("Invalid order total")

    else:
        # Child order
        if age < 18 and order_total > 100:
            parent_auth: str = input("Order is too large for your age. Do you have parental authorisation (yes/no)? ").lower()
            if parent_auth == "no":
                print("Transaction declined.")
            else:
                if has_discount == "yes":
                    print(f"Transaction of £{order_total - (order_total * 0.1)} completed")
                else:
                    print(f"Transaction of £{order_total} completed")

        # Large adult order
        elif age > 18 and order_total > 500:
            print("Additional verification required.")

        # Small adult order
        elif age > 18 and order_total <= 500:
            if has_discount == "yes":
                print(f"Transaction of £{order_total - (order_total * 0.1)} completed")
            else:
                print(f"Transaction of £{order_total} completed")
else:
    print("Please activate your account")