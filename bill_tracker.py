from bill import Bill

class BillTracker:
    # A class to track monthly bills.

    def __init__(self):
        # Initialize the bill tracker with an empty list of bills.
        self.bills = []

    def add_bill(self, bill):
        # Add a bill to the tracker.
        self.bills.append(bill)

    def get_bills(self):
        # Return a list of all bills.
        return self.bills

    def calculate_total(self):
        # Calculate the total amount of all bills.
        return sum(bill.amount for bill in self.bills)

    def remove_bill(self, bill):
        # Remove a bill from the tracker.
        bill_to_remove = bill
        self.bills = [bill for bill in self.bills if bill != bill_to_remove]

    def update_bill(self, old_bill, new_bill):
        # Update the details of a bill.
        for i, bill in enumerate(self.bills):
            if bill == old_bill:
                self.bills[i] = new_bill
                break