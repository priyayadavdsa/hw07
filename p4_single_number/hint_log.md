# Hint Log: Problem 4 (Single Number)

| Time | Level | What I tried before asking | What the hint said | What I did next |
| 4:00 | 1 | Tried [4,1,2,1,2] by hand and came up with the idea of using XOR so duplicate numbers cancel out | Yes, reasonable direction | Writing the code myself |

| 4:10 | 1 | Tried [4,1,2,1,2] by hand and came up with the idea of using XOR so duplicate numbers cancel out | Yes, reasonable direction | Writing the code myself |

## AI REVIEW
1. Edge cases it would fail on

None, provided the input matches the usual problem contract: every element appears exactly twice except one, which appears once.

Single element ([7]): 0 ^ 7 = 7, returns 7.
Negative numbers ([-1, -1, -2]): Python’s ^ works on negative ints using two’s complement semantics with arbitrary precision, so -1 ^ -1 = 0 and 0 ^ -2 = -2. Correct.
The unique number is 0 ([0, 1, 1]): result stays 0 after the pairs cancel, returns 0. Correct.
Single number at the start, middle, or end: XOR is commutative and associative, so order doesn’t matter.
Very large integers: Python ints are arbitrary precision, so there’s no overflow.

Inputs where it silently gives a wrong or meaningless answer, because they violate the contract:

Empty list: returns 0, which isn’t a valid answer, since there is no single number.
An element that appears three times, or several elements that appear an odd number of times: the result is the XOR of all odd-count values, not any one of them.
Non-integer input: floats raise TypeError on ^, and True/False would work as ints.

Those are input-validation questions, not bugs in the algorithm.

2. Complexity

Time: O(n), where n = len(nums).

The loop runs once per element.
Each iteration does one XOR on integers, which is O(1) for fixed-width values. (Strictly, for arbitrary-precision Python ints the XOR costs O(w) for w-bit numbers, but for typical bounded inputs this is treated as constant.)
No nested work, so the total is O(n).

Space: O(1).

The only extra storage is result and the loop variable num.
Nothing grows with input size, and no copy of the list is made.

3. One thing that could be clearer

The reason this works isn’t visible in the code. A short comment such as # x ^ x == 0 and x ^ 0 == x, so paired values cancel and only the unique one remains would explain the trick to a reader who hasn’t seen it. Without it, ^= looks like an arbitrary operation. Renaming result to something like unpaired would also hint at its meaning, but the comment does more.
AI agreed with my complexity claim (O(n) time, O(1) space). No disagreement.
Tested [1] (single item), printed 1 as expected