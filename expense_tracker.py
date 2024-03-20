# Create an empty dictionary to store expenses by category
expenses = {}

# Create a function for a user to add expenses
def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    
    print("Expense added successfully.")

# Create a function for that displays all expenses added by a user
def display_expenses():
    if expenses:
        print("Expense Tracker:")
        for category, amount in expenses.items():
            print(f"Category: {category} - Amount: ${amount}")
    else:
        print("No expenses recorded.")

# Create a Main function to run the program
def main():
    while True:
        print("\n1. Add an expense") #This line prints the option for the user to add expenses.
        print("2. Display all expenses") #This line prints the option for the user to display all expenses. 
        print("3. Exit")    ##This line prints the option for the user to exit.
        
        choice = input("Enter your choice: ") #this line gives the user option to enter a choice
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
