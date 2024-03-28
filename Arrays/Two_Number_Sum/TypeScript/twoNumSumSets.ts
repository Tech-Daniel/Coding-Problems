export function twoNumSumSets(numbers: number[], targetSum: number) {
  const matchingSets = new Set();

  for (let num of numbers) {
    const potentialMatch: number = targetSum - num;

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


let numbers: number[] = [1, 2, 4, 5, -5, -2];
let targetSum: number = 2;

twoNumSumSets(numbers, targetSum);
