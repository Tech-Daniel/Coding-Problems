import java.util.*;

public class TwoNumSumTwoPointers {
  public static void main(String[] args) {
    int[] numbers = new int[] {1, 2, 4, 5, -5, -2};
    int targetSum = 2;

    twoNumSum(numbers, targetSum);
  };

  public static int[] twoNumSum(int[] numbers, int targetSum) {
    Arrays.sort(numbers);
    int left = 0;
    int right = numbers.length - 1;
    
    while (left < right) {
      int currentSum = numbers[left] + numbers[right];

      if (currentSum == targetSum) {
        int[] result = new int[] {numbers[left], numbers[right]};
        System.out.println(Arrays.toString(result));
        System.out.println("You got the answer!");
        return result;
      } else if (currentSum < targetSum) {
        left ++;
      } else if (currentSum > targetSum) {
        right --;
      }
    }
    return new int[0];
  }
}
