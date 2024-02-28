def two_num_sum_two_pointers(array, target_sum):
    if len(array) < 2:
    	return []
        
    if len(array) != len(set(array)):
        raise ValueError("There is a repeated element in the given array!")
    
    array.sort()
    left, right = 0, len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            return [array[left], array[right]]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    
    return []
