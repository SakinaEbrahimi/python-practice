from expense_tracker import ExpenseTracker

is_continue = True
expense = ExpenseTracker()

while is_continue :
    print("Express Tracker")
    option = int(input("1. Add Expense \n2. View Expense \n3. Show Total Expense \n4. Search by category \n5. Exit \nChoose an option: "))
    if(option == 1):
        desc = input("Add description. ")
        amount = int(input("Add amount. "))
        category = input("Add category.")
        expense.add_expense(desc, amount, category)
    elif(option == 2):
        expense.view_expense()
    elif(option == 3):
        expense.total_expense()
    elif(option == 4):
        category = input("Enter your category. ")
        expense.search_expense_by_category(category)
    elif(option == 5):
        is_continue = False
    else:
        print("Invalid Input")
    
