balance = 0
print("Welcome to our Budget Track Program")

print("Below are the four features we offer. Please select one option at a time")

while True:
    print("1. Add Income")
    print("2. Add Expenses")
    print("3. View Balance")
    print("4. Exit")
    
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue  # Skip the rest of the loop and start over

    
    if choice == 1:
        income_amount = float(input("Enter the income amount: "))
        balance += income_amount
        print(f"income of ${income_amount} added. ")
        
    elif choice == 2:
        expense_amount = float(input("Enter the expense amount: "))
        balance -= expense_amount
        print(f"Expense of ${expense_amount} deducted. ")
        
    elif choice == 3:
        print(f"Current balance: ${balance}")
        
    elif choice == 4:
        print("Exiting the budget tracker program.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")    
         