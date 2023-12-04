# from bill_tracker import BillTracker
# from bill import Bill

# def display_menu():
#     # Display the main menu options to the user.
    
#     print("\nBill Tracker Menu:")
#     print("1. Add a Bill")
#     print("2. List all Bills")
#     print("3. Calculate Total Expenses")
#     print("4. Remove a Bill")
#     print("5. Update a Bill")
#     print("6. Exit")
#     print()

# def add_bill_ui(tracker):
#     # UI to add a bill to the tracker.
    
#     name = input("Enter bill name: ")
#     amount = float(input("Enter bill amount: "))
#     due_date = input("Enter due date (YYYY-MM-DD): ")
#     bill = Bill(name, amount, due_date)
#     tracker.add_bill(bill)
#     print("Bill added.")

# def list_bills_ui(tracker):
#     # UI to list all bills in the tracker.

#     bills = tracker.get_bills()
#     if bills:
#         print("\nList of Bills:")
#         for bill in bills:
#             print(f"{bill.name} - ${bill.amount:.2f} due on {bill.due_date}")
#     else:
#         print("No bills to display.")

# def calculate_total_ui(tracker):
#     # UI to calculate and display total expenses.
    
#     total = tracker.calculate_total()
#     print(f"\nTotal Expenses: ${total:.2f}")

# def remove_bill_ui(tracker):
#     # UI to remove a bill from the tracker.
    
#     name = input("Enter the name of the bill to remove: ")
#     found = False
#     for bill in tracker.get_bills():
#         if bill.name == name:
#             tracker.remove_bill(bill)
#             found = True
#             print("Bill removed.")
#             break
#     if not found:
#         print("Bill not found.")

# def update_bill_ui(tracker):
#     # UI to update a bill in the tracker.
    
#     name = input("Enter the name of the bill to update: ")
#     for bill in tracker.get_bills():
#         if bill.name == name:
#             new_amount = float(input("Enter new bill amount: "))
#             new_due_date = input("Enter new due date (YYYY-MM-DD): ")
#             new_bill = Bill(name, new_amount, new_due_date)
#             tracker.update_bill(bill, new_bill)
#             print("Bill updated.")
#             return
#     print("Bill not found.")

# def main():
#     tracker = BillTracker()
#     while True:
#         display_menu()
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             add_bill_ui(tracker)
#         elif choice == '2':
#             list_bills_ui(tracker)
#         elif choice == '3':
#             calculate_total_ui(tracker)
#         elif choice == '4':
#             remove_bill_ui(tracker)
#         elif choice == '5':
#             update_bill_ui(tracker)
#         elif choice == '6':
#             print("Exiting Bill Tracker.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
