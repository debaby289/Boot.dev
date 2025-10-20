"""
Fix Countdown to Launch
The countdown function should build a list of whole numbers that counts down from the starting number to 0, inclusive.

Use a while loop. If the starting number is negative, return an empty list.

Right now, the function is missing 0 and sometimes adds -1 by mistake.
"""

def countdown(start):
    numbers = []
    i = start
    while i >= 0:
        numbers.append(i)
        i -= 1
    return numbers

run_cases = [
    (5, [5, 4, 3, 2, 1, 0]),
    (1, [1, 0]),
]

submit_cases = run_cases + [
    (0, [0]),
    (-1, []),
    (3, [3, 2, 1, 0]),
    (10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input start: {input1}")
    result = countdown(input1)
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