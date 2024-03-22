import java.util.*;
import twoNumSumBruteForce;
import twoNumSumSets.twoNumSum;
import twoNumSumTwoPointers.twoNumSum;

class twoNumSumTests {
  @Test
  public void TestCase1() {
    int[] numbers = new int[] {3, 5, -4, 8, 11, -1};
    int targetSum = 10;
    int[] output = twoNumSumBruteForce(numbers, targetSum);

    Utils.assertTrue(output.length == 2);
    Utils.assertCountEqual(output, new int[] {11, -1}, "Result should contain 11 and -1.");
  }

  public boolean contains(int[] output, int value) {
    for (var el : output) {
      if (el == value) return true;
    }
    return false;
  }
}
