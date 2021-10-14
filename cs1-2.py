# Author: ATN 10/12/21

principle_investment = float(input("Please enter initial deposit amount: "))
annual_rate = float(input("Please enter the annual interest rate (as a percent): "))
time = int(input("Please enter the number of years the money is in the account: "))
number_compounded = 12
annual_rate /= 100

future_value = principle_investment * ((1 + (annual_rate / number_compounded)) ** (number_compounded * time))
print("The value at this date is " + str(future_value))
