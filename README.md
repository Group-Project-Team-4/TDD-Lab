# TDD-Lab: Monthly Bill Tracker

## Objective
Learn the principles and practices of Test-Driven Development (TDD) by building a console-based monthly bill tracker application in Python.

## Prerequisites
- Basic knowledge of Python programming.
- Familiarity with a Python IDE or text editor.
- Basic understanding of unit testing in Python (preferably 'unittest' or 'pytest').

## Tools Required
- Python 3.x
- 'unittest' or 'pytest' for writing tests.

## Optional
- Version control system (e.g., Git).

## Directory Structure
TDD-Lab/
│
├── src/
│ ├── bill.py
│ ├── bill_tracker.py
│ └── bill_tracker_console.py
│
├── tests/
│ ├── test_add_bill.py
│ ├── test_list_bills.py
│ ├── test_calculate_total.py
│ ├── test_remove_bill.py
│ └── test_update_bill.py
│
└── README.md


## Setting Up
- Ensure Python 3.x is installed on your system.
- Clone or download this repository to your local machine.
- Navigate to the 'TDD-Lab' directory.

## Running the Application
- Run the application with the command: 'python3 src/bill_tracker_console.py'
- Follow the on-screen prompts to interact with the bill tracker.

## Running the Tests
- To run all tests, use the command: 'python3 -m unittest discover -s tests'
- To run individual test files, use: 'python3 -m unittest tests/test_file_name.py'

## Interactive Lab Steps
1. **Introduction to TDD**: Understand the Red-Green-Refactor(Youtube Video below in Additional Resources) cycle and the basics of writing tests before implementation.
2. **Exploring the Application**: Familiarize yourself with the existing code in the 'src' directory.
3. **Writing Tests**: Begin by writing tests in the `tests` directory. Each test file corresponds to a specific feature of the bill tracker.
4. **Implementing Features**: Write the necessary code in the `src/bill_tracker.py` and `src/bill.py` files to pass the tests.
5. **Refactoring**: Continuously refactor the code for better structure and readability, ensuring all tests pass.
6. **Interactive Console**: Test the entire application through the `src/bill_tracker_console.py` interface.

## Additional Resources
- [Python unittest documentation](https://docs.python.org/3/library/unittest.html)
- [Article on TDD Principles](https://www.ibm.com/garage/method/practices/code/practice_test_driven_development/)
- [TDD in Python Video](https://www.youtube.com/watch?v=B1j6k2j2eJg)
