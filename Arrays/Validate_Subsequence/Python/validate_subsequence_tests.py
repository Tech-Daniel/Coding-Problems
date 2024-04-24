import unittest
from validate_subsequence_brute_force import validate_subsequence_brute_force
from validate_subsequence_two_pointers import validate_subsequence_two_pointers
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

class Test_Validate_Subsequence(unittest.TestCase):
	def setUp(self):
		"""
		Initializes the input `numbers` and the `sequence` for the test case.
		"""
		self.numbers = None
		self.sequence = None
		self.expected = None
		self.actual = None
		self.test_passed = False


	""" NORMAL/POSITIVE CASES TEST """

	def test_with_negative_and_positive_integer_sequence(self):
		"""
		Test the validate_subsequence function with Negative & Positive Integers
		"""
		self.numbers = [5, 1, 22, 25, 6, -1, 8, 10]
		self.sequence = [1, 6, -1, 10]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True

	def test_with_same_length_in_numbers_and_sequence(self):
		"""
		Test the validate_subsequence function with same length of `numbers` and `sequence`
		"""
		self.numbers = [1, 6, -1, 10]
		self.sequence = [1, 6, -1, 10]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True

	def test_with_subsequence_at_the_start_and_end(self):
		"""
		Test the validate_subsequence function with `sequence` value at the Start and the End of `numbers`
		"""
		self.numbers = [1, 22, 25, 6, -1, 8, 10]
		self.sequence = [1, 10]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True

	def test_with_duplicated_subsequence_in_numbers(self):
		"""
		Test the validate_subsequence function with Duplicated integers in `numbers`
		"""
		self.numbers = [1, 6, 1, 10, 6, 10]
		self.sequence = [1, 6, 10]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True

	def test_with_duplicated_subsequence_in_sequence(self):
		"""
		Test the validate_subsequence function with Duplicated integers in `sequence`
		"""
		self.numbers = [1, 6, -1, 10, 1, 6, 10]
		self.sequence = [1, 6, 10, 1, 6, 10]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True

	def test_with_postitive_only_integers(self):
		"""
		Test the validate_subsequence function with ONLY Positive integers 
		"""
		self.numbers = [1, 6, -1, 10, 1, 6, 10]
		self.sequence = [1, 6, 10, 1, 6, 10]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True

	def test_with_negative_only_integers(self):
		"""
		Test the validate_subsequence function with ONLY Negative integers
		"""
		self.numbers = [-5, -22, -25, -6, -1, -8, -10]
		self.sequence = [-22, -1]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True

	def test_with_ascending_order_test(self):
		"""
		Test the validate_subsequence function with Ascending orders integer
		"""
		self.numbers = [-2, 0, 1, 3, 4, 7]
		self.sequence = [0, 3, 7]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True

	def test_with_descending_order_test(self):
		"""
		Test the validate_subsequence function with Descending orders integer
		"""
		self.numbers = [8, 5, 2, -4]
		self.sequence = [8, -4]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True

	def test_false_with_incorrect_order(self):
		"""
		Test the validate_subsequence function with INCORRECT orders integer; return False
		"""
		self.numbers = [5, 1, 22, 25, 6, -1, 8, 10]
		self.sequence = [1, 6, 25, 10]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = False
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return False!")
				self.test_passed = True

	def test_false_without_existing_number(self):
		"""
		Test the validate_subsequence function without an existing integer; return False
		"""
		self.numbers = [5, 1, 6, -1, 9, 11]
		self.sequence = [1, 6, -1, 10]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = False
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return False!")
				self.test_passed = True


	""" EDGE CASES TEST """
	def test_with_repetitive_value_of_one_integers(self):
		"""
		Test the validate_subsequence function with repetitive value of one integers
		"""
		self.numbers = [1, 1, 1, 1, 1, 1]
		self.sequence = [1, 1, 1, 1]
		for validate_subsequence_func in [	validate_subsequence_brute_force,
											validate_subsequence_two_pointers]:
			with self.subTest(validate_subsequence_func=validate_subsequence_func):
				self.expected = True
				self.actual = validate_subsequence_func(self.numbers, self.sequence)

				self.assertEqual(self.actual, self.expected, "Result should return True!")
				self.test_passed = True


	def tearDown(self):
		"""
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

if __name__ == '__main__':
	unittest.main()
	
	