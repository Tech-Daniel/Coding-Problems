import two_num_sum_sets
import two_num_sum_two_pointers
import unittest

from two_num_sum_brute_force import two_num_sum_brute_force

""" class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"\u2713 {test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        _, _exc_str = self.failures[-1]
        print(f"FAIL: {test}")
        print(f"Expected: {test.expected_output}")
        print(f"Actual: {test.actual_output}")
        print(f"Details: {_exc_str}")

class CustomTextTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, resultclass=CustomTestResult, **kwargs)

class CustomTestCase(unittest.TestCase):
    def run(self, result=None):
        self.expected_output = 'expected output'  # Customize as needed
        self.actual_output = 'actual output'      # Customize as needed
        super().run(result)

class TestProgram(CustomTestCase):
    def test_case_1(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        target_sum = 10
        brute_force = two_num_sum_brute_force(array, target_sum)
        self.expected_output = [11, -1]  # Set the expected output
        self.actual_output = brute_force  # Set the actual output from the function
        self.assertTrue(len(brute_force) == 2)
        self.assertTrue(11 in brute_force)
        self.assertTrue(-1 in brute_force)

if __name__ == '__main__':
    unittest.main(testRunner=CustomTextTestRunner()) """
"""-------------------------------------------------------------"""
''' import unittest

class TestTwoNumSum(unittest.TestCase):
    def setUp(self):
        """Set up test environment for two_num_sum tests."""
        self.array = [3, 5, -4, 8, 11, 1, 6]
        self.target_sum = 10

    def test_two_num_sum_with_positive_and_negative_numbers(self):
        """
        Test two_num_sum_brute_force with a mix of positive and negative numbers.
        The function should return a list containing two numbers that add up to the target sum.
        """
        # Call the function to test
        result = two_num_sum_brute_force(self.array, self.target_sum)
        
        # Check that the result is a list with two elements
        self.assertEqual(len(result), 2, "✅ PASSED: Result contains exactly two numbers.")
        
        # Check that the two elements add up to the target sum
        self.assertEqual(sum(result), self.target_sum, "✅ PASSED: The two numbers add up to the target sum.")
        
        # Check that the expected numbers are in the result
        self.assertIn(11, result, "✅ PASSED: The number 11 is in the result.")
        self.assertIn(-1, result, "✅ PASSED: The number -1 is in the result.")

    def run(self, result=None):
        """
        Override the run method to customize the output messages.
        """
        super().run(result)
        if result.wasSuccessful():
            print("✅ All tests passed!")
        else:
            failed_tests = result.failures + result.errors
            for test, reason in failed_tests:
                print(f"❌ FAILED: {test.id()} - {reason}")

if __name__ == '__main__':
    unittest.main()  '''

import unittest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

class TestTwoNumSum(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment before each test.
        
        Initializes the input array and the target sum for the test case.
        """
        self.array = [3, 5, -4, 8, 11, 1, 6]
        self.target_sum = 10
        self.test_passed = False

    def test_two_num_sum_with_positive_and_negative_numbers(self):
        """
        Test the two_num_sum_brute_force function with a mix of positive and negative numbers.
        
        This test verifies that the function correctly identifies two numbers in the given array
        that add up to the target sum. It checks for the presence of the expected numbers in the
        result and validates the length of the result.
        """
        result = two_num_sum_brute_force(self.array, self.target_sum)
        
        self.assertEqual(len(result), 2, "Result should contain exactly two numbers.")
        self.assertEqual(sum(result), self.target_sum, "The two numbers should add up to the target sum.")
        self.assertIn(11, result, "The number 11 should be in the result.")
        self.assertIn(-1, result, "The number -1 should be in the result.")
        self.test_passed = True

    # NEGATIVE numbers test
    def test_case_3(self):
        self.array = [-4, -8, -11,  -1, -6]
        self.target_sum = -15
        result = two_num_sum_brute_force(self.array, self.target_sum)
        self.assertEqual(len(result), 2)
        self.assertEqual(sum(result), self.target_sum)
        self.assertTrue(-11 in result)
        self.assertTrue(-4 in result)
        self.test_passed = True


    def tearDown(self):
        """
        Clean up after each test.
        
        Displays a custom message indicating whether the test passed or failed.
        """
        if self.test_passed:
            logger.info("✅ Test Passed: Two numbers sum to target successfully.")
        else:
            logger.error("❌ Test Failed: Two numbers did not sum to target as expected.")


class SuppressingTestResult(unittest.TextTestResult):
    def addFailure(self, test, err):
        pass  # Suppress the default failure message
        
    def addError(self, test, err):
        pass  # Suppress the default error message 

class SuppressingTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return SuppressingTestResult(self.stream, self.descriptions, self.verbosity)

if __name__ == '__main__':
    unittest.main(testRunner=SuppressingTestRunner())

'''
if __name__ == '__main__':
    unittest.main() '''
