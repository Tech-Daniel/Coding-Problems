# Validate Subsequence
Prompt: Given two non-empty arrays of integers `array`, write a function that determines whether the second array `sequence` is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] , and so do the numbers [2, 4] . Note that a single number in an array and the array itself are both valid subsequences of the array.
<br>

## Layout:

### INPUT:
1st argument: an Array of Integers `array` 
2nd argument: an Array of Integers `sequence`
* NON-EMPTY array
* RANDOM orders && CANNOT change the orders
* REPEATABLE Integers
* NEGATIVE & POSITIVE Integers

### OUTPUT:
Return a Boolean; TRUE if `sequence` is an in-ordered subset of `array`; otherwise, FALSE.
* FALSE if it's an empty `array`

### EXAMPLE:
input1:
array1 = [5, 1, 25, 6, -1, 10]
sequence1 = [1, 6, -1, 10]

output1:
isValidSubsequence(array1, sequence1)
true

### CLARIFICAIONS:
- What are the constraints?
~   1 <= `array`.length <= 10^4
~   1 <= `sequence`.length <= 10^4
~   -10,000 <= `array[i]` <= 10,000
~   -10,000 <= `sequence`.length <= 10,000



