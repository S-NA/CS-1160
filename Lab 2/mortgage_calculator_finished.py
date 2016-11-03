## House Price Calculator
## Lab 2
## CS 1160
## Dr. Bryant

print("This program calculates how much house you can afford.")
print("Your mortgage should only be 28% of your monthly income.")

# These values make entering information easier for the user.
months_per_year = 12
max_percentage = .28  # The same as 28 percent

## Input Values 
# These are the input values for the mortgage equations we'll use.
# Feel free to change these values to try out different things.
# mortgage_years is how many years you'll pay the mortgage.
mortgage_years = 30
# interest is the interest rate from your bank (assume somewhere around 4%).
interest_rate = 4.1
# number_of_payments is how many payments you'll make for the loan.
number_of_payments = int(mortgage_years * months_per_year)
###################################################################

# This asks the user for her income and puts it in a string variable.
## \n is a *control character* that prints a new line
income = raw_input("Enter an annual net income (after taxes and deductions)\n")
# Lab Task 2C)
try:
    income = float(income)
except:
    print("You entered bad data.")
    quit() # Stop's the error from propergating futher down.
print("You entered good data.")

# This converts the string to a float (which it needs to be)

# This figures out the monthly income and monthly interest rate that are 
#  needed to calculate the user's payment.
monthly_income = income / months_per_year
interest_decimal = interest_rate / 100.0  # .041 is 4.1 percent (or 4.1 / 100)
monthly_interest = interest_decimal / months_per_year  # interest_decimal is a float

# To get the percentage of a number, multiply it times the percentage
#   For instance, 28 percent of 20000 is: .28 * 20000.
payment = monthly_income * max_percentage

## I'm *casting* these to integers before casting them to strings.
## This cuts off all the extra decimal places since I haven't showed you how 
## to get them to print to two decimal places yet.
print("Your annual income is " + str(int(income)))
print("Your maximum monthly payment is " + str(int(payment)))

## This is the big compicated mortgage equation. 
## You can break any equation down into smaller parts so they're 
## easier to work with.
numerator = monthly_interest * (1 + monthly_interest)**number_of_payments
denominator = ((1 + monthly_interest)**number_of_payments) - 1
house_price = payment / (numerator / denominator)
# print("The most expensive house you can afford costs $" + str( int(max_house_price))  )

## You can also convert all the variables into the standard variable names
##  used in the loan payment equations if it makes it easier for you.
## If you're interested in how loan payments are calculated, see: 
##     http://www.financeformulas.net/Loan_Payment_Formula.html
PV = house_price
r = monthly_interest
n = number_of_payments
P = payment
p = (r * PV) / (1 - (1 + r)**(0 - n))
print int(P)

purchase_price = raw_input("How much is the house you want to buy?\n")
# Lab Task 2C
try:
    purchase_price = float(purchase_price)  # converts to a float
except:
    print "You entered bad data."
    quit() # Stop's the error from propergating futher down.
print "You entered good data."

#################################################################
#################################################################
#####  Task 2.A.) Enter your code here
#################################################################
if purchase_price >= house_price + 100000:
    print("Yeah right...dream on.")
elif purchase_price >= house_price + 50000:
    print("Maybe when you get a promotion.")
elif purchase_price > house_price:
    print("You can almost afford it.")
elif purchase_price <= house_price:  # at least or less than, we can afford.
    print("Yes, you can afford this house.")

#################################################################
#################################################################
#####  Task 2.B.) Enter your code here
#################################################################	
## Now we print out an amortization / payment schedule, or how the user's loan goes down
## over time based on that house price.

current_balance = purchase_price

# Table header.
# Source for format documentation: https://pyformat.info/
# Formatting starts becoming ugly when numbers get into the millions.
print "Payment      Balance                 Toward interest         Toward principal:"
for i in range(number_of_payments):
    interest_part = monthly_interest * current_balance
    principal_part = payment - interest_part
    dataForTable = ( i
                   , current_balance
                   , interest_part
                   , principal_part
                   )
    print("{0:03d}        {1:12.3f}         {2:12.3f}             {3:12.3f}".format(*dataForTable)) # prints out a single row, and formats it. * is the prefix the denotes raw.
    current_balance = current_balance - principal_part
print("Complete.")

#################################################################
#################################################################
#####  Task 2.C.) Enter your code around the raw_input( ) functions above
#################################################################
##### Done twice: cat mortgage_calculator_finished.py | grep raw_input | head -n 2 -
