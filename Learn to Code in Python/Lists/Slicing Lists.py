"""
Assignment
Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:
    First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
    Next, return a slice of the champions list that starts at the beginning of the list and includes all champions except for the very last champion.
    Last, return a slice of the champions list that only includes the champions in even numbered indexes.

Tip
Remember, you can return multiple values from a function by separating them with commas:
return value1, value2, value3
"""

def get_champion_slices(champions):
    list1 = champions[2:]
    list2 = champions[:-1]
    list3 = champions[::2]
    champions = list1,list2,list3
    return champions  

    #Simple Option
    #return champions[2:], champions[:-1], champions[::2]


run_cases = [
    (
        ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad", "Gilforn"],
        (
            ["Gandolfo", "Thraine", "Norwad", "Gilforn"],
            ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad"],
            ["Thrundar", "Gandolfo", "Norwad"],
        ),
    ),
    (
        ["Frank", "Dennis", "Sweet Dee", "Mac", "Charlie"],
        (
            ["Sweet Dee", "Mac", "Charlie"],
            ["Frank", "Dennis", "Sweet Dee", "Mac"],
            ["Frank", "Sweet Dee", "Charlie"],
        ),
    ),
]

submit_cases = run_cases + [
    (([]), ([], [], [])),
    (
        (["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon", "Tony"]),
        (
            ["Spencer", "Bill", "Matthew", "Brandon", "Tony"],
            ["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon"],
            ["John", "Spencer", "Matthew", "Tony"],
        ),
    ),
]


def test(input1, expected_output):
    print("-" * 40)
    print(f"Input:\n{input1}")
    print(f"Expected:\n{expected_output}")
    try:
        slice_1, slice_2, slice_3 = get_champion_slices(input1)
        result = (slice_1, slice_2, slice_3)
    except Exception as e:
        print(f"Error: {e}")
        return False
    print(f"Actual:\n{result}")
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