def max_difference_indices(nums):
    if not nums or len(nums) < 2:
        return "No valid pair"

    min_index = 0
    max_diff = 0
    result = "No valid pair"

    for i in range(1, len(nums)):
        if nums[i] > nums[min_index]:
            diff = nums[i] - nums[min_index]
            if diff > max_diff:
                max_diff = diff
                result = [min_index, i]
        elif nums[i] < nums[min_index]:
            min_index = i  # Update min_index to the new lowest value

    return result

# Example usage:
print(max_difference_indices([1, 5, 3, 4, 2]))  # Output: [0, 1]
print(max_difference_indices([3, 3, 3, 3]))    # Output: "No valid pair"
