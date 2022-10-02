import math

principal = float(input("Enter the loan principal:\n"))
store = input('What do you want to calculate? \n'
             'type "m" - for number of monthly payments,\n' 
             'type "p" - for the monthly payment:\n').lower()
if store == "m":
    monthly_payments = float(input("Enter the monthly payment:\n"))
    rest_month = math.ceil(principal / monthly_payments)
    if rest_month > 1:
        print("It will take " + str(rest_month) + " months to repay the loan")
    else:
        print("It will take " + str(rest_month) + " month to repay the loan")
elif store == "p":
    periods = float(input("Enter the number of months:\n"))
    payment = math.ceil(principal / periods)
    lastpayment = math.ceil(principal - ((periods - 1) * payment))
    if payment % periods == 0:
        print("Your monthly payment = ", payment)
    elif payment % periods != 0:

        print("Your monthly payment = " + str((payment)) + " and the last payment = " + str(lastpayment))




