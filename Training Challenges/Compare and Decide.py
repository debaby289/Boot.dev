"""
Compare and Decide
Complete three small functions that practice comparisons and boolean logic. They return True/False or a short string based on simple rules.

is_eligible_driver(age, has_permit)
    Return True if age is 16 or older AND has_permit is True.
    Otherwise return False.
within_safe_temp(temp)
    Return True if temp is between 68 and 77 inclusive.
    Otherwise return False.
better_score(a, b)
    Return "A" if a is greater than b.
    Return "B" if b is greater than a.
    Return "Tie" if they are equal.
"""

def is_eligible_driver(age, has_permit):
    if age >= 16 and has_permit == True:
        return True
    else:
        return False

def within_safe_temp(temp):
    if 68 <= temp <= 77:
        return True
    else:
        return False

def better_score(a, b):
    if a > b:
        return "A"
    elif a < b:
        return "B"
    else:
        return "Tie"

from main import is_eligible_driver, within_safe_temp, better_score

# Run cases (happy paths)
run_driver_cases = [
    (16, True, True),
    (15, True, False),
]

run_temp_cases = [
    (68, True),
    (80, False),
]

run_better_cases = [
    (10, 9, "A"),
    (7, 7, "Tie"),
]

# Submit cases
submit_driver_cases = run_driver_cases + [
    (20, False, False),
    (17, True, True),
    (0, False, False),  # edge: very young
]

submit_temp_cases = run_temp_cases + [
    (77, True),   # edge: upper bound
    (67, False),  # edge: just below lower bound
    (72, True),
]

submit_better_cases = run_better_cases + [
    (3, 8, "B"),
    (-1, -1, "Tie"),  # edge: equal negatives
    (42, 0, "A"),     # satisfying happy path
]


def test_driver(age, has_permit, expected):
    print("---------------------------------")
    print(f"Input:\n  age: {age}\n  has_permit: {has_permit}")
    result = is_eligible_driver(age, has_permit)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def test_temp(temp, expected):
    print("---------------------------------")
    print(f"Input temperature: {temp}")
    result = within_safe_temp(temp)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def test_better(a, b, expected):
    print("---------------------------------")
    print(f"Input scores:\n  A: {a}\n  B: {b}")
    result = better_score(a, b)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0

    # Choose which set to run
    driver_cases = submit_driver_cases
    temp_cases = submit_temp_cases
    better_cases = submit_better_cases

    if "__RUN__" in globals():
        driver_cases = run_driver_cases
        temp_cases = run_temp_cases
        better_cases = run_better_cases

    print("Testing is_eligible_driver...")
    for case in driver_cases:
        if test_driver(*case):
            passed += 1
        else:
            failed += 1
    print()

    print("Testing within_safe_temp...")
    for temp, expected in temp_cases:
        if test_temp(temp, expected):
            passed += 1
        else:
            failed += 1
    print()

    print("Testing better_score...")
    for a, b, expected in better_cases:
        if test_better(a, b, expected):
            passed += 1
        else:
            failed += 1
    print()

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


main()
