# Problem 2: Valid Anagram
# Input: two strings, s and t
# Output: True if t is an anagram of s (same letters, same counts), otherwise False
# Time:  O(n)
# Space: O(k), k = number of distinct characters (at most min(n, alphabet size))
#        O(n) in the general case, O(1) if only lowercase a-z (k <= 26)
# Reason: two separate loops, each going once over a string of length n, so the
#         work is about 2n, which is O(n). The dictionary has one entry per
#         distinct character, so its size depends on the alphabet, not on n alone.
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        if count.get(ch, 0) == 0:
            return False
        count[ch] -= 1
    return True

print(is_anagram("listen", "silent"))
print(is_anagram("cat", "car"))
print(is_anagram("", ""))

print(is_anagram("a", "ab"))