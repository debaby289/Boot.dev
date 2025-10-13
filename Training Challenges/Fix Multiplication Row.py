"""
Fix Multiplication Row
The multiplication_row function should return the first ten multiples of a number using a loop.

Expected behavior:
Given an integer n, return a list of 10 numbers: [n*1, n*2, ..., n*10]
Always start at n*1 and end at n*10
Right now the function includes an extra value and starts at the wrong place.

Examples:
print(multiplication_row(3))
# Expected: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

print(multiplication_row(1))
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

What to do:
    Fix the loop so it builds exactly 10 values.
    Start from 1 * n and end at 10 * n.
    Use a loop, no list comprehensions.
"""

def multiplication_row(n):
    products = []
    for i in range(1, 11):
        products.append(n * i)
    return products

run_cases = [
    (3, [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]),
    (1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    (7, [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]),
]

submit_cases = run_cases + [
    (0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    (-4, [-4, -8, -12, -16, -20, -24, -28, -32, -36, -40]),
    (12, [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input number: {input1}")
    result = multiplication_row(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
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