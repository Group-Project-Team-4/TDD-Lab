class Bill:
    # A class representing a single bill.

    def __init__(self, name, amount, due_date):
        """
        Initialize a new Bill instance.

        Args:
            name (str): The name of the bill.
            amount (float): The amount due for the bill.
            due_date (str): The due date of the bill.
        """
        self.name = name
        self.amount = amount
        self.due_date = due_date

    def __repr__(self):
        # A string representation of a Bill instance.
        return f"Bill(name='{self.name}', amount={self.amount:.2f}, due_date='{self.due_date}')"