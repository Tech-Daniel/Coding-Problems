import java.util.*;

class twoNumSumSets {
  public static void main(String[] args) {
    int [] numbers = new int[] {1, 2, 4, 5, -5, -2};
    int targetSum = 2;

    twoNumSum(numbers, targetSum);
  };

  public static int[] twoNumSum(int[] numbers, int targetSum) {
    Set<Integer> nums = new HashSet<>();
    for (int num : numbers) {
      int potentialMatch = targetSum - num;
      if (nums.contains(potentialMatch)) {
        int[] result = new int[] {num, potentialMatch};
        System.out.println(Arrays.toString(result));
        System.out.println("You got the answer!");
        return result;
      } else {
        nums.add(num);
      }
    } 
    return new int[0];
  }
};