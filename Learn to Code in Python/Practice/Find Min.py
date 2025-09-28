"""
Assignment
Write a function called find_min() that finds the smallest number in a list. For example:
    find_min([1, 3, -1, 2]) -> -1
    find_min([18, 3, 7, 2]) -> 2
"""

def find_min(nums):
    # start with infinity so any number will be smaller
    min_value = float("inf")
    
    for num in nums:
        if num < min_value:
            min_value = num  # update min_value when a smaller number is found
    
    return min_value

run_cases = [
    ([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7], -4),
    ([4, 3, 2, 1, 18, 1, 2, 3, 4, 5, 6, 7], 1),
]

submit_cases = run_cases + [
    ([43, 234, 65465, 234, 2343, 443, 2123, 8768], 43),
    ([0], 0),
    ([-1, -2, -3], -3),
    ([100, 200, 300], 100),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = find_min(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
