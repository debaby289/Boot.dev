# python
nums = [3, -2, 7, 4]  # assume non-empty
current_max = nums[0]

for x in nums[1:]:
    if x > current_max:
        current_max = x

print(current_max)