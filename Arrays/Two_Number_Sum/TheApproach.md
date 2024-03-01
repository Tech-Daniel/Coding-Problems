## Intuition:
The intuition for the Two Number Sum problem can be approached from three perspectives: brute force, time optimization, and space optimization.

### Brute Force Approach: 
The most straightforward approach is to use two nested loops to iterate over each pair of numbers in the array. For each pair, we check if their sum equals the target sum. This approach has a time complexity of O(n^2) and a space complexity of O(1), as we are not using any additional data structures. However, this approach is not efficient for large arrays because it checks every possible pair of numbers.

### Time Optimization: 
To improve the time complexity, we can use a Set or a Hashmap (Dictionary). We iterate over the array once, and for each number, we calculate its complement (i.e., target sum - current number). If the complement is in the Set or Hashmap, we have found the pair that sums up to the target. If not, we add the current number to the Set or Hashmap. This approach has a time complexity of O(n) and a space complexity of O(n), as we are using a Set or Hashmap to store the numbers. This approach is more efficient than the brute force approach, especially for large arrays, as it only requires a single pass through the array.

### Space Optimization: 
If we want to optimize for space, we can sort the array first, which takes O(n log n) time. Then, we use two pointers, one at the start of the array and one at the end. We calculate the sum of the numbers at the two pointers. If the sum equals the target, we have found the pair. If the sum is less than the target, we move the left pointer to the right. If the sum is greater than the target, we move the right pointer to the left. We repeat this process until the pointers meet. This approach has a time complexity of O(n log n) due to the sorting, and a space complexity of O(1), as we are not using any additional data structures. This approach is efficient in terms of space, but it requires the array to be sorted first, which may not be desirable in some cases
<br>

#### Approach 1: Brute Force
In this approach, we use two nested loops to check every possible pair of numbers in the array to see if they add up to the target sum.
1. Initialize an empty list to store the result.
2. Loop through each element i in the array using the first loop.
3. Inside the first loop, start another loop from the element next to i to the end of the array.
4. In the inner loop, check if the sum of the current pair of elements equals the target sum.
5. If it does, add the numbers of these two elements to the result list.
6. Return the result list if a pair is found, or an empty list if no pair adds up to the target sum.  

#### Approach 2: Hash Table
This approach uses a hash table to reduce the overall time complexity by avoiding the second loop.
1. Create an empty dictionary to store the numbers and their indices.
2. Loop through each element in the array.
3. For each element, calculate the complement by subtracting the current element from the target sum.
4. Check if the complement is already in the dictionary.
5. If it is, return a list containing the number of the complement from the dictionary and the current index.
6. If the complement is not found, store the current element in the dictionary.

#### Approach 3: Sorting and Two Pointers
This approach involves sorting the array and using two pointers to find the pair.
1. Sort the array while keeping track of the original indices.
2. Initialize two pointers, one at the start (left) and one at the end (right) of the array.
3. While the left pointer is less than the right pointer:
    - Calculate the sum of the elements at the left and right pointers.
    - If the sum is equal to the target, return an array with original of the two numbers.
    - If the sum is less than the target, move the left pointer to the right to increase the sum.
    - If the sum is greater than the target, move the right pointer to the left to decrease the sum.
4. If no pair is found, return an empty list.
