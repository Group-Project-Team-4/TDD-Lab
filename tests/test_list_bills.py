import unittest
from src.bill_tracker import BillTracker
from src.bill import Bill

class TestListBills(unittest.TestCase):
    # Test suite for listing all bills in the BillTracker.
    
    def setUp(self):
        # Set up a fresh instance of BillTracker for each test.
        self.tracker = BillTracker()

    def test_list_bills(self):
        # Test if the BillTracker can list all added bills. 
        # This test adds a single bill and then checks if the list of bills contains exactly one bill.
        bill = Bill('Internet', 50, '2023-05-15')
        self.tracker.add_bill(bill)
        self.assertEqual(self.tracker.get_bills(), [bill])

if __name__ == '__main__':
    unittest.main()
