"""
Max in List
A list is an ordered collection of items, like [3, 7, 2].
A loop lets you visit each item in the list one by one.
Hints:

Think about a variable that keeps track of your current best answer.
Consider how you compare each new item to that current best.
"""

# python
nums = [3, -2, 7, 4]  # assume non-empty
current_max = nums[0]

for x in nums[1:]:
    if x > current_max:
        current_max = x

print(current_max)