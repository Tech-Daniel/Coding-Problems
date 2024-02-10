def two_num_sum_brute_force(array, target_sum):
    for first_idx in range(len(array) - 1):
        for second_idx in range(first_idx + 1, len(array)):
			first_num = array[first_idx]
            second_num = array[second_idx]
			if first_num + second_num == target_sum:
                return [first_num, second_num]
    return []


