# Two Number Sum
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty
array.

Note: The target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.
--------------------------------------------------------------------
## Intuition:
The intuition behind the Two Number Sum problem can be approached from three perspectives: brute force, time optimization, and space optimization.

#### Brute Force Approach: 
The most straightforward approach is to use two nested loops to iterate over each pair of numbers in the array. For each pair, we check if their sum equals the target sum. This approach has a time complexity of O(n^2) and a space complexity of O(1), as we are not using any additional data structures. However, this approach is not efficient for large arrays because it checks every possible pair of numbers.
