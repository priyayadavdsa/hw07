# Problem 4: Single Number
# Input: a list of integers (nums) where every number appears twice except one
# Output: the number that appears only once
# Time:  O(n)
# Space: O(1)
# Reason: one loop over the list with no nesting, so n steps in total.
#         Only one variable (result) is used, so extra memory does not grow.

def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


nums = [4, 1, 2, 1, 2]

print("Single number:", singleNumber(nums))

print(singleNumber([2, 2, 1]))
print(singleNumber([1]))