import unittest
from bill_tracker import BillTracker
from bill import Bill

class TestAddBill(unittest.TestCase):
    # Test suite for adding bills to the BillTracker.
    
    def setUp(self):
        # Set up a fresh instance of BillTracker for each test.
        self.tracker = BillTracker()

    def test_add_bill(self):
        # Test if a new bill can be added to the BillTracker.
        # It verifies that the bill is correctly added by checking its presence in the list of bills.
        bill = Bill('Electricity', 100, '2023-05-20')
        self.tracker.add_bill(bill)
        self.assertIn(bill, self.tracker.get_bills())

if __name__ == '__main__':
    unittest.main()
