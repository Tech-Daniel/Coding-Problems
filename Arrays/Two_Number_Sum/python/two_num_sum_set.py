def two_num_sum_set(array, target_sum):
	nums = set()
	for num in array:
		potential_match = target_sum - num
		if potential_match in nums:
			return [potential_match, num]
		else:
			nums.append(potential_match)
	return []