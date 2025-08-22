def dutch_national_flag(nums):
    low, mid, high = 0, 0, len(nums) - 1  # Three pointers

    while mid <= high:
        if nums[mid] == 0:  # Blue (swap to the left)
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:  # Red (correct place, move ahead)
            mid += 1
        else:  # nums[mid] == 2 (White, swap to the right)
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1  # Move high pointer left

# Example usage:
nums = [2, 0, 2, 1, 1, 0, 2, 1, 0, 0, 1, 2]
dutch_national_flag(nums)
print(nums) 
