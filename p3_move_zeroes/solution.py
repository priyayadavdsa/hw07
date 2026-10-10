# Problem 3: Move Zeroes
# Input: a list of integers (nums)
# Output: the same list with all 0s moved to the end, other numbers keeping their order
# Time:  O(n)
# Space: O(1)
# Reason: one loop over the list with no nested loop, so n steps in total.
#         The swap is done in place, so no extra list or dictionary is created.

def moveZeroes(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    return nums


nums = [0, 1, 0, 3, 12]

moveZeroes(nums)

print("Array after moving zeros:", nums)

print(moveZeroes([0]))