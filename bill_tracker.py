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
        return sum(bill['amount'] for bill in self.bills)

    def remove_bill(self, bill):
        # Remove a bill from the tracker.
        if bill in self.bills:
            self.bills.remove(bill)

    def update_bill(self, old_bill, new_bill):
        # Update the details of a bill.
        try:
            index = self.bills.index(old_bill)
            self.bills[index] = new_bill
        except ValueError:
            pass
