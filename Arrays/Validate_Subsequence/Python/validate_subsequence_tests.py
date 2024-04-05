import unittest
import validate_subsequence_brute_force
import validate_subsequence_two_pointers
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
		self.test_passed = False

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
	
	