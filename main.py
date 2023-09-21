loan_amount = float(input("Enter loan amount: "))
payment_amount = float(input("Enter payment amount: "))
interest_rate = float(input("Enter interest rate: "))

# Initializew variables
current_balance = loan_amount
num_payments = 0
 
# Check if the payment amount is less than the interest accrued
while current_balance > 0:
    interest_accrued = current_balance * interest_rate
    current_balance = current_balance + interest_accrued
    current_balance = current_balance - payment_amount
    num_payments = num_payments + 1
    
if num_payments != 1:
    print(f"{num_payments} payments")
else:
    print(f"{num_payments} payment")
