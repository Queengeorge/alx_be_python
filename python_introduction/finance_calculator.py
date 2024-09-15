monthly_income = input("enter your monthly income: ")
total_monthly_expenses = input ("Enter your total monthly expenses: ")
monthly_savings = float(monthly_income) - float(total_monthly_expenses)
print("your monthly savings is $",monthly_savings)

annual_savings = monthly_savings * 12
interest_rate = 0.05
projected_savings = annual_savings + (annual_savings * interest_rate)

print("projected savings after one year, with interest, is: $",projected_savings)





                       