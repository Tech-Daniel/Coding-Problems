function twoNumSumTwoPointers(numbers, targetSum) {
  numbers.sort((a,b) => a-b);
  let left = 0;
  let right = numbers.length - 1

  while (left < right) {
    let num1 = numbers[left];
    let num2 = numbers[right];
    let currentSum = num1 + num2;

    if (currentSum < targetSum) {
      left ++;
    } else if (currentSum > targetSum) {
      right --;
    } else {
      let result = [num1, num2];
      console.log(result);
      console.log("You got it!");
      return result;
    }
  }
  return [];
}

let numbers = [1, 2, 4, 5, -5, -2];
let targetSum = 2;

twoNumSumTwoPointers(numbers, targetSum);


