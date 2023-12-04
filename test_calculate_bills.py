import unittest
from bill_tracker import BillTracker
from bill import Bill

class TestCalculateBills(unittest.TestCase):
    #Test suite for calculating the total amount of all bills in the BillTracker.
    
    def setUp(self):
        # Set up a fresh instance of BillTracker for each test.
        self.tracker = BillTracker()

    def test_calculate_total_expenses(self):
        # Test if the BillTracker correctly calculates the total expenses.
        # This test adds multiple bills and then verifies if the calculated total matches the expected sum.
        self.tracker.add_bill(Bill('Water', 30, '2023-05-10'))
        self.tracker.add_bill(Bill('Gas', 40, '2023-05-05'))
        self.assertEqual(self.tracker.calculate_total(), 70)

if __name__ == '__main__':
    unittest.main()
