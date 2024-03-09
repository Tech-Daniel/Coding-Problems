import unittest
from two_num_sum_brute_force import two_num_sum_brute_force
from two_num_sum_sets import two_num_sum_sets
from two_num_sum_two_pointers import two_num_sum_two_pointers
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
        self.numbers = None
        self.target_sum = None
        self.test_passed = False

    """ POSITIVE/NORMAL TEST CASES """

    def test_two_num_sum_with_mixed_numbers(self):
        """Test functions with a mix of positive & negative numbers."""
        self.numbers = [3, 5, -4, 8, 11, -1, 6]
        self.target_sum = 10
        
        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                result = two_num_sum_func(self.numbers, self.target_sum)

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
        self.numbers = [-4, -8, -11, -1, -6]
        self.target_sum = -15
        
        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                result = two_num_sum_func(self.numbers, self.target_sum)
        
                self.expected = (2, self.target_sum)  # Expected length and sum
                self.actual = (len(result), sum(result))  # Actual length and sum
                
                self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
                self.assertCountEqual(result, [-11, -4], "Result should contain -11 and -4.")
                self.test_passed = True

    def test_with_positive_numbers_and_multiple_answers(self):
        """
        Test the two_num_sum_brute_force function with positive numbers and multiple correct answers.
        """
        self.numbers = [3, 5, 8, 11, 0, 6]
        self.target_sum = 11
        
        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                result = two_num_sum_func(self.numbers, self.target_sum)

                self.expected = (2, self.target_sum)  # Expected length and sum
                self.actual = (len(result), sum(result))  # Actual length and sum
                
                self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
                self.assertIn(result, ([0, 11], [11, 0], [5, 6], [6, 5], [3, 8], [8, 3]), "Result should be one of the valid number pairs.")
                self.test_passed = True

    def test_with_descending_numbers(self):
        """
        Test the two_num_sum_brute_force function with descending numbers.
        """
        self.numbers = [9, 8, 7, 6, 5, 4, 3, 0, -3, -5]
        self.target_sum = 0
        
        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                result = two_num_sum_func(self.numbers, self.target_sum)

                self.expected = (2, self.target_sum)  # Expected length and sum
                self.actual = (len(result), sum(result))  # Actual length and sum
                
                self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
                self.assertIn(result, ([5, -5], [-5, 5], [3, -3], [-3, 3]), "Result should be one of the valid number pairs.")
                self.test_passed = True

    def test_with_ascending_number(self):
        """
        Test the two_num_sum with ascending numbers.
        """
        self.numbers = [-6, -3, -1, 0, 3, 7, 9]
        self.target_sum = 10

        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                result = two_num_sum_func(self.numbers, self.target_sum)
        
                self.expected = (2, self.target_sum)  # Expected length and sum
                self.actual = (len(result), sum(result))  # Actual length and sum
                
                self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
                self.assertCountEqual(result, [3, 7], "Result should contain 3 and 7.")
                self.test_passed = True

    def test_with_negative_sum(self):
        """
        Test the two_num_sum with negative sum.
        """
        self.numbers = [-1, -2, -3, -4, -5]
        self.target_sum = -9

        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                result = two_num_sum_func(self.numbers, self.target_sum)
        
                self.expected = (2, self.target_sum)  # Expected length and sum
                self.actual = (len(result), sum(result))  # Actual length and sum
                
                self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
                self.assertCountEqual(result, [-4, -5], "Result should contain -4 and -5.")
                self.test_passed = True

    
    """ EDGE CASES TEST """

    def test_without_existing_sum(self):
        """
        Test the two_num_sum without existing sum.
        """
        self.numbers = [3, 5, -4, 8, 11, 1, -1, 6]
        self.target_sum = 30
        
        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                result = two_num_sum_func(self.numbers, self.target_sum)
        
                self.expected = ([])  # Expected empty array
                self.actual = (result)  # Actual length and sum
                
                self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
                self.test_passed = True

    def test_with_large_numbers(self):
        """
        Test the two_num_sum with large numbers.
        """
        self.numbers = [2147483647, -2147483648]
        self.target_sum = -1

        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                result = two_num_sum_func(self.numbers, self.target_sum)
        
                self.expected = (2, self.target_sum)  # Expected length and sum
                self.actual = (len(result), sum(result))  # Actual length and sum
                
                self.assertEqual(self.actual, self.expected, "The two numbers should add up to the target sum and result should contain exactly two numbers.")
                self.assertCountEqual(result, [2147483647, -2147483648], "Result should contain 2147483647 and -2147483648.")
                self.test_passed = True


    """ NEGATIVE/INPUT VALIDATION CASE TESTS """

    def test_with_input_integer_type_for_numbers_arg(self):
        """
        Test the two_num_sum with integer type from `numbers` argument.
        """
        self.numbers = 100
        self.target_sum = -1

        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                with self.assertRaises(TypeError) as handler:
                    two_num_sum_func(self.numbers, self.target_sum)
                
                self.expected = f"Expected a list, got {type(self.numbers)}"
                self.actual = str(handler.exception)
                
                self.assertEqual(self.actual, self.expected)
                self.test_passed = True

    def test_with_input_null_type_for_numbers_arg(self):
        """
        Test the two_num_sum with null type from `numbers` argument.
        """
        self.numbers = None
        self.target_sum = 14

        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                with self.assertRaises(TypeError) as handler:
                    two_num_sum_func(self.numbers, self.target_sum)
                
                self.expected = f"Expected a list, got {type(self.numbers)}"
                self.actual = str(handler.exception)
                
                self.assertEqual(self.actual, self.expected)
                self.test_passed = True
    
    def test_with_input_null_type_for_elements_inside_numbers_arg(self):
        """
        Test the two_num_sum with null type for element in `numbers` argument.
        """
        self.numbers = [-1, -5, 0, None, 15]
        self.target_sum = 14

        for two_num_sum_func in [two_num_sum_brute_force, 
                                 two_num_sum_sets, 
                                 two_num_sum_two_pointers]:
            with self.subTest(two_num_sum_func=two_num_sum_func):
                with self.assertRaises(TypeError) as handler:
                    two_num_sum_func(self.numbers, self.target_sum)
                
                self.expected = "All elements in `numbers` must be integers"
                self.actual = str(handler.exception)
                
                self.assertEqual(self.actual, self.expected)
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
