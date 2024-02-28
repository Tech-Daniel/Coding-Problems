
def two_num_sum_sets(array, target_sum):
	''' nums = set()
	for num in array:
		potential_match = target_sum - num
		if potential_match in nums:
			return [potential_match, num]
		else:
			nums.add(potential_match)
	return [] '''

	if len(array) < 2:
		return []
	
	if len(array) != len(set(array)):
		raise ValueError("There is a repeated element in the given array!")

	dict = {}

	for num in array:
		potentialMatch = target_sum - num

		if potentialMatch in dict:
			return [potentialMatch, num]
		else:
			dict[num] = "Matching Number"
	return []
