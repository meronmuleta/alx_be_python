Monthly_income = int(input("Enter your monthly income: "))
Monthly_expenses = int(input("Enter your total monthly expenses: "))
Monthly_savings = Monthly_income - Monthly_expenses
Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)
print("Your monthly savings are " + "$" + str(Monthly_savings))
print("Projected savings after one year, with interest, is: " + "$" + str(Projected_savings))
