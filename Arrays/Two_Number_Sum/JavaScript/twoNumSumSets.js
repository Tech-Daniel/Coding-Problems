function twoNumSumSets(numbers, targetSum) {
  const matchingSets = new Set();

  for (let num of numbers) {
    const potentialMatch = targetSum - num;
    if (matchingSets.has(potentialMatch)) {
      console.log([num, potentialMatch]);
      console.log("You got it!");
      return [num, potentialMatch];
    } else {
      matchingSets.add(num);
    }
  }
  return [];
}

let numbers = [1, 2, 4, 5, -5, -2];
let targetSum = 2;

twoNumSumSets(numbers, targetSum);
