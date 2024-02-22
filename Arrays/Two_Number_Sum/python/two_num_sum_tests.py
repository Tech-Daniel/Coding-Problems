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
        self.array = [3, 5, -4, 8, 11, -1, 6]
        self.target_sum = 10
        self.test_passed = False

    def test_with_positive_and_negative_numbers(self):
        """
        Test the two_num_sum_brute_force function with a mix of positive and negative numbers.
        
        This test verifies that the function correctly identifies two numbers in the given array
        that add up to the target sum. It checks for the presence of the expected numbers in the
        result and validates the length of the result.
        """
        result = two_num_sum_brute_force(self.array, self.target_sum)

        self.expected = (2, self.target_sum)  # Expected length and sum
        self.actual = (len(result), sum(result))  # Actual length and sum
        
        self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
        self.assertIn(11, result, "The number 11 should be in the result.")
        self.assertIn(-1, result, "The number -1 should be in the result.")
        self.test_passed = True

    def test_with_all_negative_numbers(self):
        """
        Test the two_num_sum_brute_force function with all negative numbers.
        """
        self.array = [-4, -8, -11, -1, -6]
        self.target_sum = -15
        result = two_num_sum_brute_force(self.array, self.target_sum)

        self.expected = (2, self.target_sum)  # Expected length and sum
        self.actual = (len(result), sum(result))  # Actual length and sum
        
        self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
        self.assertCountEqual(result, [-11, -4], "Result should contain -11 and -4.")
        self.test_passed = True

    def test_with_positive_numbers_and_multiple_answers(self):
        """
        Test the two_num_sum_brute_force function with positive numbers and multiple correct answers.
        """
        self.array = [3, 5, 8, 11, 0, 6]
        self.target_sum = 11
        result = two_num_sum_brute_force(self.array, self.target_sum)

        self.expected = (2, self.target_sum)  # Expected length and sum
        self.actual = (len(result), sum(result))  # Actual length and sum
        
        self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
        self.assertIn(result, ([0, 11], [11, 0], [5, 6], [6, 5], [3, 8], [8, 3]), "Result should be one of the valid number pairs.")
        self.test_passed = True

    def test_with_descending_numbers(self):
        """
        Test the two_num_sum_brute_force function with descending numbers.
        """
        self.array = [9, 8, 7, 6, 5, 4, 3, 0, -3, -5]
        self.target_sum = 0
        result = two_num_sum_brute_force(self.array, self.target_sum)

        self.expected = (2, self.target_sum)  # Expected length and sum
        self.actual = (len(result), sum(result))  # Actual length and sum
        
        self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
        self.assertIn(result, ([5, -5], [-5, 5], [3, -3], [-3, 3]), "Result should be one of the valid number pairs.")
        self.test_passed = True

    def test_with_ascending_number(self):
        """
        Test the two_num_sum with ascending numbers.
        """
        self.array = [-6, -3, -1, 0, 3, 7, 9]
        self.target_sum = 10
        result = two_num_sum_brute_force(self.array, self.target_sum)
        
        self.expected = (2, self.target_sum)  # Expected length and sum
        self.actual = (len(result), sum(result))  # Actual length and sum
        
        self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
        self.assertCountEqual(result, [3, 7], "Result should contain 3 and 7.")
        self.test_passed = True

    
    ## EDGE CASES TEST
    # NON_EXISTING sum test
    def test_without_existing_sum(self):
        """
        Test the two_num_sum without existing sum.
        """
        self.array = [3, 5, -4, 8, 11, 1, -1, 6]
        self.target_sum = 30
        result = two_num_sum_brute_force(self.array, self.target_sum)
        
        self.expected = ([])  # Expected empty array
        self.actual = (result)  # Actual length and sum
        
        self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
        self.test_passed = True

    # Large numbers test
    def test_with_large_numbers(self):
        """
        Test the two_num_sum with large numbers.
        """
        self.array = [2147483647, -2147483648]
        self.target_sum = -1
        result = two_num_sum_brute_force(self.array, self.target_sum)
        
        self.expected = (2, self.target_sum)  # Expected length and sum
        self.actual = (len(result), sum(result))  # Actual length and sum
        
        self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
        self.assertCountEqual(result, [2147483647, -2147483648], "Result should contain 2147483647 and -2147483648.")
        self.test_passed = True


    def tearDown(self):
        """
        Clean up after each test.
        
        Logs a message indicating whether the test passed or failed, including the test method name.
        If the test failed, logs the expected and actual output.
        """
        test_method_name = self.id().split('.')[-2:]
        class_name, method_name = test_method_name
        full_test_name = f"{class_name}.{method_name}"
        
        if self.test_passed:
            logger.info(f"✅ Test Passed: {full_test_name}")
        else:
            logger.error(f"❌ Test Failed: {full_test_name} - Expected: {self.expected}, Actual: {self.actual}")

'''
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
    unittest.main() 
