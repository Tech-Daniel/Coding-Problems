def validate_subsequence_two_pointers(numbers, sequence):
	arr_idx = 0
	seq_idx = 0
	while arr_idx < len(numbers) and seq_idx < len(sequence):
		if numbers[arr_idx] == sequence[seq_idx]:
			seq_idx += 1
		arr_idx += 1
	
	print(f"The answer is {seq_idx == len(sequence)}")
	return seq_idx == len(sequence)

# numbers = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# validate_subsequence_two_pointers(numbers, sequence)
