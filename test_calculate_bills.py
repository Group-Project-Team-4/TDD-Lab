import unittest
from bill_tracker import BillTracker

class TestCalculateTotal(unittest.TestCase):
    #Test suite for calculating the total amount of all bills in the BillTracker.
    
    def setUp(self):
        # Set up a fresh instance of BillTracker for each test.
        self.tracker = BillTracker()

    def test_calculate_total_expenses(self):
        # Test if the BillTracker correctly calculates the total expenses.
        # This test adds multiple bills and then verifies if the calculated total matches the expected sum.
        self.tracker.add_bill({'name': 'Water', 'amount': 30, 'due_date': '2023-05-10'})
        self.tracker.add_bill({'name': 'Gas', 'amount': 40, 'due_date': '2023-05-05'})
        self.assertEqual(self.tracker.calculate_total(), 70)

if __name__ == '__main__':
    unittest.main()
