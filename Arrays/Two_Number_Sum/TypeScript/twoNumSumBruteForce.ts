export function twoNumSumBruteForce(numbers: number[], targetSum: number) {
  for (let i: number = 0; i < numbers.length - 1; i++) {
    let firstNum: number = numbers[i];
    for (let j: number = i + 1; j < numbers.length; j++) {
      let secondNum: number = numbers[j];

      if (firstNum + secondNum == targetSum) {
        console.log([firstNum, secondNum])
        console.log("You got it!")
        return [firstNum, secondNum];
      };
    }
  }
  return [];
}

let numbers: number[] = [1, 2, 4, 5, -5, -2];
let targetSum: number = 2;

twoNumSumBruteForce(numbers, targetSum);

