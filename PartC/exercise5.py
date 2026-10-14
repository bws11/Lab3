loan_amount: float = float(input("How much is your loan? £"))
an_interest_rate: float = float(input("How much is your interest rate (as a decimal, e.g. 10% -> 0.1)? "))
repayment_period: int = int(input("How long is your repayment period in years? "))

if loan_amount <= 0 or repayment_period <= 0:
    print("Invalid input")
else:
    total_payments = repayment_period * 12

    if an_interest_rate == 0:
        monthly_repayment = loan_amount / total_payments
    else:
        mo_interest_rate = an_interest_rate / 100 / 12
        monthly_repayment: float = loan_amount * mo_interest_rate (((1 + mo_interest_rate) ** total_payments) / (((1 + mo_interest_rate) ** total_payments) - 1))

    print(f"Monthly payment: {round(monthly_repayment, 2)}")
    print(f"Total amount to be repaid: {total_payments * monthly_repayment}")
    print(f"Total Interest: {loan_amount * an_interest_rate}")