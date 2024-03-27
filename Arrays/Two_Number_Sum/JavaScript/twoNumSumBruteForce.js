function twoNumSumBruteForce(numbers, targetSum) {
  for (let i = 0; i < numbers.length - 1; i++) {
    const firstNum = numbers[i];
    
    for (let j = i + 1; j < numbers.length; j++) {
      const secondNum = numbers[j];

      if (firstNum + secondNum == targetSum) {
        console.log([firstNum, secondNum])
        console.log("You got it!")
        return [firstNum, secondNum];
      };
    };
  };
  return [];
}

let numbers = [1, 2, 4, 5, -5, -2];
let targetSum = 2;

twoNumSumBruteForce(numbers, targetSum);


exports.twoNumSumBruteForce = twoNumSumBruteForce;
