"""
Assignment
Complete the find_missing_ids function. It accepts two lists as input, and returns a new set of all the IDs that are in the first list but are not in the second.

Naturally, there will be no duplicates in the resulting set.
"""

def find_missing_ids(first_ids, second_ids):
    #Empty sets
    set1 = set()
    set2 = set()
    set3 = set()
    
    for first in first_ids:
        set1.add(first)
    
    for second in second_ids:
        set2.add(second)

    #substraction
    set3 = set1 - set2
    return set3

run_cases = [
    ([1, 1, 1, 2, 2, 2, 3], [1, 2], {3}),
    ([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 5, 6, 7, 8], {9, 10}),
]

submit_cases = run_cases + [
    ([], [], set()),
    ([1, 1, 1], [], {1}),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], set()),
    ([1, 1, 2, 2, 3, 3], [1, 2, 3], set()),
    ([1, 2, 3, 4, 5], [1, 2, 3], {4, 5}),
    ([1, 2, 3, 4, 5], [1, 3, 5], {2, 4}),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f" - first_ids:  {input1}")
    print(f" - second_ids: {input2}")
    result = find_missing_ids(input1, input2)
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