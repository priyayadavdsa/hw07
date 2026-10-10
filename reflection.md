# Failure Analysis

## Hardest problem: Problem 2 (Valid Anagram)

**My first approach:**
I had no complete plan at first. I understood the examples ("listen" and "silent" is True, "cat" and "car" is False), but I could not think of a way to check this in code. After I got a hint to count how many times each letter appears, I started writing the code.

**Why I thought it would work:**
I thought that once I had the length check and the counting loop for the first word, the function was finished.

**Why it failed:**
I had only written the length check and the counting loop for s. I had not written the loop that checks t against the counts, and I had no final return True. When I ran it, all three test lines printed None, because a Python function with no return gives back None.

**How I found the problem:**
I looked at the terminal output (None, None, None) and compared it with the expected output (True, False, True). I saw that my function stopped after the first loop.

**What I did next:**
I added a second loop over t. It returns False if a letter is missing or its count is 0, and otherwise subtracts 1 from the count. I also added return True at the end. After that the output matched: True, False, True.

**What I learned:**
A function can run without any error and still give the wrong result, so I should test it and read the actual output before assuming it works.

# Reflection

I got stuck most when turning my idea into code.

The hardest problem for me was Valid Anagram because because I did not know how to count letters in code.

I learned that using AI as a hint means the hint should only guide my next thought, and I should write and test the code myself.

Next time I get stuck, I will try on paper for 15 minutes first, then ask for a Level 1 hint before asking for more.