import two_num_sum_brute_force
import two_num_sum_sets
import two_num_sum_two_pointers

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        target_sum = 10
        brute_force = two_num_sum_brute_force(array, target_sum)
        self.assertTrue(len(brute_force) == 2)
        self.assertTrue(11 in brute_force)
        self.assertTrue(-1 in brute_force)

