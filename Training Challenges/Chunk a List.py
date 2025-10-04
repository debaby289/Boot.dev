"""
Chunk a List
Complete the chunk_list function.

Given a list of items and a positive chunk size, return a new list where the items are grouped into sublists of length size (the last chunk may be shorter if there aren’t enough items left).

Rules:
    If size is less than 1, return an empty list [].
    Do not modify the input list.
    Use loops to build the result
"""

def chunk_list(items, size):
    chunks = []

    if size < 1:
        return []

    for i in range(0, len(items), size):  
        chunk = items[i:i + size]         
        chunks.append(chunk)               
    return chunks

run_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [[1, 2, 3], [4, 5, 6], [7]]),
    (["x", "y", "z"], 1, [["x"], ["y"], ["z"]]),
    ([10, 20, 30], 5, [[10, 20, 30]]),
]

submit_cases = run_cases + [
    ([], 4, []),
    ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
    ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
    ([42], 0, []),
]


def test(items, size, expected_output):
    print("---------------------------------")
    print(f"Input items: {items}")
    print(f"Chunk size:  {size}")
    result = chunk_list(items, size)
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