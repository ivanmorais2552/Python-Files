expenseList = []

expenses = float(input(("Enter an expense or 0 to finish: ")))

while expenses != 0:
    if expenses < 0:
        print("Invalid expense. Please enter a positive amount.")
    elif expenses > 0:
        expenseList.append(expenses)
    expenses = float(input(("Enter an expense or 0 to finish: ")))
else:
    totalNumExpenses = len(expenseList)
    totalExpenses = sum(expenseList)
    averageExpenses = totalExpenses / totalNumExpenses if totalNumExpenses > 0 else 0
    smallestExpense = min(expenseList)
    biggestExpense = max(expenseList)

    print("Expense Summary")
    print("===================")
    print("\nNumber of expenses: " + str(totalNumExpenses))
    print("Total: " + "${:,.2f}".format(totalExpenses))
    print("Average expense: " + "${:,.2f}".format(averageExpenses))
    print("Smallest expense: " + "${:,.2f}".format(smallestExpense))
    print("Largest expense: " + "${:,.2f}".format(biggestExpense))
    print("Number of small expenses: " +
          str(len([expense for expense in expenseList if expense < 25])))
    print("Number of medium expenses: " +
          str(len([expense for expense in expenseList if 25 <= expense <= 100])))
    print("Number of large expenses: " +
          str(len([expense for expense in expenseList if expense > 100])))
    print("\n===================")
