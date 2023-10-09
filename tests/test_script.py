import sys
import os

# Get the current script's directory (tests directory)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (my_project directory)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to sys.path
sys.path.append(parent_dir)
print(sys.path)

# Now you can import modules from the parent directory
from src.isPrime import checkIsPrime

import unittest

class TestFunctions(unittest.TestCase):

    def testPrime(self):
        result = checkIsPrime(5)
        self.assertTrue(result == True)
    
if __name__ == '__main__':
    unittest.main()

# Testing 
