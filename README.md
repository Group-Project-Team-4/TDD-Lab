# TDD-Lab: Monthly Bill Tracker

## Objective
Experience the Test-Driven Development (TDD) process by building a console-based monthly bill tracker application in Python, starting with failing tests and gradually implementing features to make them pass.

## Prerequisites
- Basic knowledge of Python programming.
- Familiarity with a Python IDE or text editor.
- Basic understanding of unit testing in Python (preferably `unittest` or `pytest`).

## Tools Required
- Version control system (e.g., Git).
- Python 3.x
- `unittest` or `pytest` for writing tests.

## Directory Structure
```
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
```

## Setting Up
- Ensure Python 3.x is installed on your system, run `python3 --version`. (Download link below) 
- Navigate to the location where you would like to save this project.
- Clone or download this repository to your local machine, run `git clone "URL to code"`.
- Navigate to the `TDD-Lab` directory.
- Initially, the source files under `src/` will have their contents commented out.


## Interactive Lab Steps
1. **Watch and Learn TDD**: Start by gaining a basic understanding of Test Driven Development. Watch the following video (about 15mins)
   - [TDD in Python Video](https://www.youtube.com/watch?v=B1j6k2j2eJg)

2. **Running the Failing Tests**: Then run the test suite. The tests are expected to fail initially since the implementation is commented out.
   - Run the tests using the command: `python3 -m unittest discover -s tests`
   - Observe the failing tests.

3. **Implementing Features**:
   - Begin by uncommenting the contents of `src/bill.py` and `src/bill_tracker.py`.
   - After uncommenting each file, rerun the tests to see the changes in test results.
   - Aim to get all tests passing by uncommenting and, if necessary, modifying the source files.

4. **Interacting with the Console Application**:
   - Once all tests are passing, uncomment the contents of `src/bill_tracker_console.py`.
   - Run the console application with: `python3 src/bill_tracker_console.py`
   - Interact with the application to manually test its functionality.

## Additional Resources
- [Python3 Download](https://www.python.org/downloads/)
- [Git Download](https://git-scm.com/downloads)
- [Python unittest documentation](https://docs.python.org/3/library/unittest.html)
