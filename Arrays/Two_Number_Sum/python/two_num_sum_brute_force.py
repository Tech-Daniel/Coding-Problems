def two_num_sum_brute_force(numbers, target_sum):
    """
    Finds two numbers in a list that sum up to a target sum.

    Args:
        numbers (list): A list of integers to search through.
        target_sum (int): The target sum to find.

    Returns:
        list: A list containing the two numbers that add up to the target_sum,
              or an empty list if no such numbers exist.
    """
    validate_input(numbers, target_sum)

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return [numbers[i], numbers[j]]
    return []

def validate_input(numbers, target_sum):
    """
    Validates the input parameters.

    Args:
        numbers (list): The list of numbers to validate.
        target_sum (int): The target sum to validate.

    Raises:
        TypeError: If `numbers` is not a list or `target_sum` is not an integer.
        ValueError: If `numbers` contains duplicates or less than two elements.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list, got {type(numbers)}")
    if len(numbers) < 2:
        raise ValueError("At least two numbers required in `numbers`")
    if len(numbers) != len(set(numbers)):
        raise ValueError("Duplicate integers found in `numbers`")
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("All elements in `numbers` must be integers")
    if not isinstance(target_sum, int):
        raise TypeError(f"Expected an int for `target_sum`, got {type(target_sum)}")
    