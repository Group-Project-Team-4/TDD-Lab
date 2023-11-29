import unittest
from bill_tracker import BillTracker

class TestListBills(unittest.TestCase):
    # Test suite for listing all bills in the BillTracker.
    
    def setUp(self):
        # Set up a fresh instance of BillTracker for each test.
        self.tracker = BillTracker()

    def test_list_bills(self):
        # Test if the BillTracker can list all added bills. 
        # This test adds a single bill and then checks if the list of bills contains exactly one bill.
        self.tracker.add_bill({'name': 'Internet', 'amount': 50, 'due_date': '2023-05-15'})
        self.assertEqual(len(self.tracker.get_bills()), 1)

if __name__ == '__main__':
    unittest.main()
