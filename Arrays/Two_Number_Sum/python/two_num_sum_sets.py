def two_num_sum_sets(array, target_sum):
	nums = set()
	for num in array:
		potential_match = target_sum - num
		if potential_match in nums:
			return [potential_match, num]
		else:
			nums.add(potential_match)
	return []