#  Problem 1: Contains Duplicate
# Input: a list of integers (nums)
# Output: True if any value appears more than once, otherwise False
#
# Time:  O(n^2)
# Space: O(1)
# Reason: the outer loop runs over n items and the inner loop checks the items
#         after it, so there are about n*(n-1)/2 comparisons. No list, set or
#         dictionary is created, so the extra memory stays constant.
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([]))

print(contains_duplicate([5]))