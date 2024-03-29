export function twoNumSumTwoPointers(numbers: number[], targetSum: number) {
  numbers.sort((a,b) => a-b);
  let left: number = 0;
  let right: number = numbers.length - 1

  while (left < right) {
    let num1: number = numbers[left];
    let num2: number = numbers[right];
    let currentSum: number = num1 + num2;
    if (currentSum == targetSum) {
      let result = [num1, num2];
      console.log(result);
      console.log("You got it!");
      return result;
    } else if (currentSum < targetSum) {
      left ++;
    } else if (currentSum > targetSum) {
      right --;
    }
  }
  return [];
}

let numbers: number[] = [1, 2, 4, 5, -5, -2];
let targetSum: number = 2;

twoNumSumTwoPointers(numbers, targetSum);
