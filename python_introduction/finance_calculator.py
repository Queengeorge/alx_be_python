monthly_income = input("enter your monthly income: ")
total_monthly_expenses = input ("Enter your total monthly expenses: ")
monthly_savings = int(monthly_income) - int(total_monthly_expenses)
print("your monthly savings is $",monthly_savings)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("projected savings after one year, with interest, is: $",projected_savings)





                       