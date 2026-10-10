# Hint Log: Problem 3 (Move Zeroes)

| Time | Level | What I tried before asking | What the hint said | What I did next |
| 3:22 | 1 | Tried [0,1,0,3,12] by hand on paper and wrote my idea in first_approach.md | Yes, my direction was reasonable | Starting to write the code myself |

## AI REVIEW
1. Edge cases it would fail on

None. It correctly moves all zeros to the end while keeping the non-zero elements in their original relative order.

Empty list: the loop never runs, returns [].
Single element ([0] or [5]): [0] stays [0]; for [5], it swaps nums[0] with itself and returns [5].
All zeros ([0, 0, 0]): the condition is never true, so nothing changes.
No zeros ([1, 2, 3]): every element is non-zero, so j always equals i and each swap is a self-swap. The list is unchanged, which is correct.
Zeros at the start, middle, or end: j always points at the first zero in the processed prefix, so each non-zero found is swapped into it. Order of non-zeros is preserved because i and j only move forward.
Negative numbers: != 0 handles them.
0.0 and False: both compare equal to 0, so they are treated as zeros. That’s fine for numeric input, but worth knowing if the list can hold mixed types.

Two behaviors to be aware of, neither a bug:

It mutates the input in place and also returns it. If the problem says “do not return anything,” returning nums is harmless but unnecessary.
It performs self-swaps when i == j, which are wasted writes but not errors.

2. Complexity

Time: O(n), where n = len(nums).

The loop runs exactly n iterations, one pass.
Each iteration does a comparison, a swap, and an increment, all O(1).
j only moves forward and never causes any rescanning, so there is no nested work. Total: O(n).

Space: O(1).

Only the variables i and j are used, and the swap is done with a tuple assignment on existing elements.
Python’s range is lazy, so no index list is built.
The modification is in place, so no copy of the list is made. (The returned value is a reference to the same list, not new memory.)

3. One thing that could be clearer

The role of j is not obvious from its name. It is the “write position”: the index where the next non-zero element belongs, and everything before it is already non-zero. Renaming it to something like write_idx or adding a comment such as # j = next slot for a non-zero value would make the two-pointer invariant readable at a glance without changing the approach.

AI agreed with my complexity claim (O(n) time, O(1) space). No disagreement.
Tested [0] (single zero), printed [0] as expected.