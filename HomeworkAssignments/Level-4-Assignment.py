# Create List to store expenses
expenseList = []

# Prompt user for expenses
fExpense = float(input(("Enter an expense or 0 to finish: ")))

# Loop to collect expenses until user enters 0
while fExpense != 0:
    if fExpense < 0:
        print("Invalid expense. Please enter a positive amount.")
    elif fExpense > 0:
        expenseList.append(fExpense)
    fExpense = float(input(("Enter an expense or 0 to finish: ")))

else:
    totalNumExpenses = len(expenseList)
    totalExpenses = sum(expenseList)
    averageExpenses = totalExpenses / totalNumExpenses if totalNumExpenses > 0 else 0
    smallestExpense = min(expenseList)
    biggestExpense = max(expenseList)

# Print the summary of expenses
    print("Expense Summary")
    print("===================")
    print("\nNumber of expenses: " + str(totalNumExpenses))
    print("Total: " + "${:,.2f}".format(totalExpenses))
    print("Average expense: " + "${:,.2f}".format(averageExpenses))
    print("Smallest expense: " + "${:,.2f}".format(smallestExpense))
    print("Largest expense: " + "${:,.2f}".format(biggestExpense))
    print("Number of small expenses: " +
          str(len([fExpense for fExpense in expenseList if fExpense < 25])))
    print("Number of medium expenses: " +
          str(len([fExpense for fExpense in expenseList if 25 <= fExpense <= 100])))
    print("Number of large expenses: " +
          str(len([fExpense for fExpense in expenseList if fExpense > 100])))
    print("\n===================")
