# Two Number Sum
Prompt: Write a function that takes in a non-empty [array] of distinct integers and an integer representing a [target_sum]. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty
array.

Note: The target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.
<br>

## Layouts:

### INPUT:
1st parameter: an INTEGER ARRAY [array].
2nd parameter: an INTEGER [target_sum].
* Unique/Distinct Integer elements in the array
* Non-empty Integer Array
* Random orders
* Negative and Positive Integers

### OUTPUT:
Return an INTEGER ARRAY with TWO values that sum up to [target_sum].
* Return in ANY orders
* Each element in the return array must be UNIQUE
* If no sum exists, return an empty_array []

### Example:
Input:
array = [1, 5, 2, 7, -4, 0, -9]
target_sum = 9

Output:
[2, 7]

### CLARIFICATIONS:
- What are the constraints?
  - Max & Min Length of the [array]
  - Max & Min Integer values of the [array][i]
  - Max & Min Integer values of the [target_sum]

* NEGATIVE Case Tests
- How do you handle [array].length LESS than 2?
- How do you handle duplicated values in [array]?
- How do you handle incorrect [array] data Type other than List Type?
- How do you handle incorrect [array][i] elements data Type other than Integer Type?
- How do you handle incorrect [target_sum] data Type other than Integer Type?

