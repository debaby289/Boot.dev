"""
Flatten Task Schedule
Complete the flatten_tasks function.

You’re given a list of task blocks (a list of lists). Each inner list contains tasks in the order they should be done. Return a single, flat list of all tasks in order.
    Preserve the order of tasks as they appear from left to right, top to bottom.
    Ignore empty blocks.
    Do not modify the input.
    Use loops to build the result.
Suggested approach:
    Create an empty list for the result.
    Loop over each block in the outer list.
    For each block, loop over its tasks and append them to the result list.
    Return the result list.
"""

def flatten_tasks(blocks):
    #new list to hold flattened tasks
    new_list = []

    #loop through each block in the list of blocks
    for block in blocks:
        #loop through each task in the block
        for b in block:
            new_list.append(b)
    return new_list

run_cases = [
    (
        [["write", "review"], ["commit"], ["push"]],
        ["write", "review", "commit", "push"],
    ),
    (
        [[1, 2, 3], [4], [], [5, 6]],
        [1, 2, 3, 4, 5, 6],
    ),
    (
        [["morning"], ["noon", "evening"]],
        ["morning", "noon", "evening"],
    ),
]

submit_cases = run_cases + [
    (
        [],
        [],
    ),
    (
        [[], [], []],
        [],
    ),
    (
        [["a"], [], ["b", "c"], [], ["d"]],
        ["a", "b", "c", "d"],
    ),
    (
        [[True, False], ["x"], [0, 1, 0]],
        [True, False, "x", 0, 1, 0],
    ),
]


def test(input_blocks, expected_output):
    print("---------------------------------")
    print(f"Input blocks: {input_blocks}")
    result = flatten_tasks(input_blocks)
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
