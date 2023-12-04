import unittest
from src.bill_tracker import BillTracker
from src.bill import Bill

class TestRemoveBill(unittest.TestCase):

    def setUp(self):
        self.tracker = BillTracker()

    def test_remove_bill(self):
        bill = Bill('Cable', 20, '2023-05-25')
        self.tracker.add_bill(bill)
        self.tracker.remove_bill(bill)
        self.assertNotIn(bill, self.tracker.get_bills())

if __name__ == '__main__':
    unittest.main()
