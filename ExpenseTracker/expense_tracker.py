from datetime import date
from prettytable import PrettyTable 

class ExpenseTracker:
    def __init__(self):
        self.expenses = [] 

    def add_expense(self,description, amount, category):
        if(amount > 0):
            today_date = date.today()
            self.expenses.append(dict(Date = (today_date.year, today_date.month, today_date.day),Description = description, Amount = amount, Category = category))
            return
        else:
            print("Invalid input")

    def view_expense(self):
        if not self.expenses:
            print("There is not any expenses.")
        table = PrettyTable(['Date', 'Description', 'Amount', 'Category'])
        for expense in self.expenses :
            table.add_row([expense['Date'], expense['Description'], expense['Amount'], expense['Category']])

        print(table)

    def total_expense(self):
        if not self.expenses:
            print("There is not any expenses.")

        total = 0
        for expense in self.expenses:
            total += expense['Amount']
        
        print(f"The total expenses is: {total}")

    def search_expense_by_category(self,category):
        if not category:
            print("Category does not exist.")

        if not self.expenses:
            print("There is not any expenses.")

        table = PrettyTable(['Date', 'Description', 'Amount', 'Category'])
        for expense in self.expenses:
            if(expense['Category'] == category):
                table.add_row([expense['Date'], expense['Description'], expense['Amount'], expense['Category']])
            
        print(table)
        




        

        

