"""
Name: Landon Badgett
interest.py

Problem: Print hello world

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def main():
    interest_rate = eval(input("Enter the annual interest rate: "))
    days_in_cycle = eval(input("Enter the number of days in the billing cycle: "))
    previous_balance = eval(input("Enter the previous (net) balance: "))
    pmt = eval(input("Enter the payment amount: "))
    payment_date = eval(input("Enter the day in the billing cycle the payment was made: "))
    step1 = previous_balance * days_in_cycle
    step2 = pmt * (days_in_cycle - payment_date)
    step3 = step1 - step2
    step4 = step3 / days_in_cycle
    monthly_rate = (interest_rate / 100) / 12
    monthly_interest_rate = step4 * monthly_rate
    print(round(monthly_interest_rate, 2))
if __name__ == '__main__':
    main()
