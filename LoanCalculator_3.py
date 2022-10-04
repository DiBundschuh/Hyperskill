import math

"""    n = month(principal, monthly_payment, interest)
    a = annuity(principal, num_periods, interest),
    p = loan(monthly_payment ,num_periods, interest)
"""

def annuity(P, n, i): #annuity rate

    A = P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    return A

def month(P, A, i): #number of payments
    const = A / (A - i * P)
    n = math.log(const, 1+i)
    return n
def loan(A, n, i): #prinicipal
    P = A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))

    return P


store = input('What do you want to calculate? \n'
              'type "n" - for number of monthly payments,\n'
              'type "a" for annuity monthly payment amount,\n'
              'type "p" - for the monthly payment:\n').lower()

if store == "n":
    principal = float(input("Enter the loan principal:\n"))
    monthly_payment = float(input("Enter the monthly payment:\n"))
    interest = (float(input("Enter the loan interest:\n"))/(12*100))
    m = month(principal, monthly_payment, interest)
    m = int(math.ceil(m))
    
    years = math.floor(m / 12)

    mon = math.ceil(m % 12)
    print(m, years, mon)
    
    if years >= 1 and mon != 0:
        print("It will take {} years and {} months to repay this loan!".format(years, mon))
    elif years >= 1 and mon == 0:
        print("It will take {} years to repay this loan!".format(years))
    elif years == 1 and mon != 0:
        print("It will take {} year and {} months to repay this loan!".format(years, mon))
    elif years == 1 and mon == 0:
        print("It will take {} year to repay this loan!".format(years))
    elif years == 0 and mon != 0:
        print("It will take {} months to repay this loan!".format(mon))
    elif years == 0 and mon <= 1:
        print("It will take {} month to repay this loan!".format(mon))
    else:
        print("Something went wrong!")

elif store == "a":
    principal = float(input("Enter the loan principal:\n"))
    num_periods = float(input("Enter the number of periods:\n"))
    interest = (float(input("Enter the loan interest:\n"))/(12*100))
    a = annuity(principal, num_periods, interest)
    print("Your monthly payment = {}!".format(math.ceil(a)))

elif store == "p":
    monthly_payment = float(input("Enter the monthly payment:\n"))
    num_periods = float(input("Enter the number of periods:\n"))
    interest = (float(input("Enter the loan interest:\n"))/(12*100))
    p = loan(monthly_payment, num_periods, interest)
    print("Your loan principal = {}!".format(math.ceil(p)))
