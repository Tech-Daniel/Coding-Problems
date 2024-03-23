import java.util.*;
TwoNumSumBruteForce bruteForceSolution = new TwoNumSumBruteForce();
TwoNumSumSets setsSolution = new TwoNumSumSets();
TwoNumSumTwoPointers twoPointersSolution = new TwoNumSumTwoPointers();

class TwoNumSumTests {
  @Test
  public static void TestCase1() {
    int[] numbers = new int[] {3, 5, -4, 8, 11, -1};
    int targetSum = 10;
    int[] output = bruteForceSolution.twoNumSum(numbers, targetSum);

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
