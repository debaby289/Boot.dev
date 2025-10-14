"""
Number the Tasks
Complete the number_tasks function.

Given a list of task names (strings), return a new list where each task is prefixed with its number starting from 1.

Use a for loop
Keep the original task text as-is
The format should be: "<number>. <task>"
Tip: You can use enumerate(iterable, start=1) to get both the index (starting at 1) and the value in a loop
"""

def number_tasks(tasks):
    task_list = []
    for i, task in enumerate(tasks, start=1):
        formatted_task = f"{i}. {task}"
        task_list.append(formatted_task)
    return task_list

run_cases = [
    (["Buy milk", "Train"], ["1. Buy milk", "2. Train"]),
    (["Quest", "Collect 10 herbs", "Defeat Rat"], ["1. Quest", "2. Collect 10 herbs", "3. Defeat Rat"]),
    ([], []),
]

submit_cases = run_cases + [
    (["Single"], ["1. Single"]),
    (["  spaces  "], ["1.   spaces  "]),
    (["Cook", "Eat", "Sleep", "Repeat"], ["1. Cook", "2. Eat", "3. Sleep", "4. Repeat"]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input tasks: {input1}")
    result = number_tasks(input1)
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