import unittest
from bill_tracker import BillTracker
from bill import Bill

class TestRemoveBill(unittest.TestCase):
    # Test suite for updating bill details in the BillTracker.
    
    def setUp(self):
        # Set up a fresh instance of BillTracker for each test.
        self.tracker = BillTracker()

    def test_remove_bill(self):
        # Test if a bill's details can be updated in the BillTracker.
        # This test adds a bill, updates it, and then checks if the updated bill is present and the old bill is absent.
        bill = Bill('Cable', 20, '2023-05-25')
        self.tracker.add_bill(bill)
        self.tracker.remove_bill(bill)
        self.assertNotIn(bill, self.tracker.get_bills())

if __name__ == '__main__':
    unittest.main()
