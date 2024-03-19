import java.util.*;

class twoNumSumBruteForce {
  public static void main(String[] args) {
    int [] numbers = new int[] {1, 2, 4, 5, -5, -2};
    int targetSum = 2;

    twoNumSum(numbers, targetSum);
  };
  
  public static int[] twoNumSum(int[] numbers, int targetSum) {
    for (int i = 0; i < numbers.length - 1; i++) {
      int firstNum = numbers[i];
      for (int j = i + 1; j < numbers.length; j++) {
        int secondNum = numbers[j];
        
        if (firstNum + secondNum == targetSum) {
          int[] result = new int[] {firstNum, secondNum};
          System.out.println(Arrays.toString(result));
          System.out.println("You got the answer!");
          return new int[] {firstNum, secondNum};
        }
      }
    }
    // System.out.println(new int[0]);
    return new int[0];
  };
};
