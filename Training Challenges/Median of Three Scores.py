"""
Median of Three Scores
Complete three functions that work together to rank three player scores without using loops or collections.

Implement the following in main.py:
    min_of_three(a, b, c) → returns the smallest value
    median_of_three(a, b, c) → returns the middle value (the median)
    max_of_three(a, b, c) → returns the largest value
Constraints:
    Do not use loops (for, while).
    Do not use collections (list, dict, set) or built-ins like sorted().
    Use only variables, comparisons, and simple conditionals.
Behavior details:
    Handle duplicate values correctly. For example, the median of (7, 7, 3) is 7, and of (10, 10, 10) is 10.
    Negative numbers should work as expected.
"""

def min_of_three(a, b, c):
    if (a >= b) and (b <= c):
        return b
    elif (b >= c) and (c <= a):
        return c
    elif (c >= a) and (a <= b):
        return a
        
def median_of_three(a, b, c):
    # Max --- Min
    if ((a <= b) or (a <= c)) and ((a >= b) or (a >= c)):
        return a
    elif ((b <= a) or (b <= c)) and ((b >= a) or (b >= c)):
        return b
    elif ((c <= b) or (c <= a)) and ((c >= b) or (c >= a)):
        return c

def max_of_three(a, b, c):
    if a >= b:
        return a
    elif b >= c:
        return b
    elif c >= a:
        return c
    
    run_cases = [
    ((5, 7, 9), (5, 7, 9)),
    ((9, 5, 7), (5, 7, 9)),
    ((7, 7, 3), (3, 7, 7)),
]

submit_cases = run_cases + [
    ((-1, -5, -3), (-5, -3, -1)),
    ((10, 10, 10), (10, 10, 10)),
    ((42, 7, 19), (7, 19, 42)),
]


def test(triple, expected_tuple):
    a, b, c = triple
    print("---------------------------------")
    print(f"Input: (a={a}, b={b}, c={c})")
    result_tuple = (
        min_of_three(a, b, c),
        median_of_three(a, b, c),
        max_of_three(a, b, c),
    )
    print(f"Expected: (min={expected_tuple[0]}, median={expected_tuple[1]}, max={expected_tuple[2]})")
    print(f"Actual:   (min={result_tuple[0]}, median={result_tuple[1]}, max={result_tuple[2]})")
    if result_tuple == expected_tuple:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for triple, expected in test_cases:
        correct = test(triple, expected)
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