"""
Assignment
Some of our players would like to view their inventories in reverse order.

Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

For example:
[1, 2, 3] -> [3, 2, 1]
['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']
"""

def reverse_list(items):
    n = len(items) - 1
    newList = []
    for i in range(n, -1, -1):
        newList.append(items[i])
    return newList

run_cases = [
    (
        ["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"],
        ["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"],
    ),
    ([1, 2, 300, 4, 5], [5, 4, 300, 2, 1]),
]

submit_cases = run_cases + [
    ([], []),
    (["a"], ["a"]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (
        ["apple", "banana", "cherry", "date", "elderberry"],
        ["elderberry", "date", "cherry", "banana", "apple"],
    ),
    (["hello", "world"], ["world", "hello"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input list: {input}")
    print(f"Expected reversed list: {expected_output}")
    result = reverse_list(input)
    print(f"Actual reversed list: {result}")
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
