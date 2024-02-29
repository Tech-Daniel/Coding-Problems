# TIME: O(n); where n is the numbers in the array
# SPACE: O(n); where n is the numbers in the set()

def two_num_sum_sets(array, target_sum):
	if len(array) < 2:
		return []
	
	if len(array) != len(set(array)):
		raise ValueError("There is a repeated element in the given array!")
	
	nums = set()
	for num in array:
		potential_match = target_sum - num
		if num in nums:
			return [potential_match, num]
		else:
			nums.add(potential_match)
	return [] 

	
