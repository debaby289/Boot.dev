""""
Score Summary
Complete the score_summary function.

Given a list of integer scores, return three values in this order:

The smallest score
The largest score
The average score rounded to 2 decimal places
If the list is empty, return (0, 0, 0).
"""

def score_summary(scores):
    if not scores:
        return 0, 0, 0

    smallest = min(scores)
    largest = max(scores)
    average = round(sum(scores) / len(scores), 2)
    return smallest, largest, average

run_cases = [
    ([10, 20, 30], (10, 30, 20.0)),
    ([5, 5, 5, 5], (5, 5, 5.0)),
    ([3, 1, 2, 4], (1, 4, 2.5)),
]

submit_cases = run_cases + [
    ([], (0, 0, 0)),
    ([42], (42, 42, 42.0)),
    ([-5, -1, -3, -2], (-5, -1, -2.75)),
    ([100, 50, 75, 25, 0], (0, 100, 50.0)),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input scores: {input1}")
    result = score_summary(input1)
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