def validate_subsequence(numbers, sequence):
	subset_remainder = len(numbers)
	numbers_check = 0
	sequence_check = 0
	# print(f"The subsequence is {subset_remainder == 0}!")
	# print("You got the answer!")

	while 0 < subset_remainder and numbers_check < len(numbers):
		num = numbers[numbers_check]
		seq_num = sequence[sequence_check]

		if num == seq_num:
			subset_remainder -= 1
			numbers_check += 1
			sequence_check += 1
			continue
		else:
			numbers_check += 1
	
	print(f"The subsequence is {subset_remainder == 0}!")
	print("You got the answer!")
	return subset_remainder == 0


numbers = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
validate_subsequence(numbers, sequence)

