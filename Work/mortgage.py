# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months_to_repay = 0

extra_payment_start_month = 10
extra_payment_end_month = 19
extra_payment = 1000

while principal > 0:
    repayment = payment
    if months_to_repay >= extra_payment_start_month and months_to_repay <= extra_payment_end_month:
        repayment = payment + extra_payment
    principal = principal * (1 + rate/12) - repayment

    if principal < 0:
        repayment = repayment + principal
        principal = 0
    
    total_paid = total_paid + repayment
    months_to_repay = months_to_repay + 1
    print(months_to_repay, repayment, principal, total_paid)

print("Total paid", total_paid)
print("Months to repay", months_to_repay)

