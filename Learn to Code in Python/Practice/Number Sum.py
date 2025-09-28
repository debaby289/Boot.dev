"""
Assignment
Complete the number_sum function. It should add up all the numbers from 1 to n and return the result. For example:
    number_sum(5) -> 1+2+3+4+5 -> 15
    number_sum(3) -> 1+2+3 -> 6
"""

def number_sum(n):
    s = n + 1
    sum = 0
    for i in range(1,s):
        sum += i 
    return sum

run_cases = [
    (3, 6),
    (5, 15),
]

submit_cases = run_cases + [
    (1, 1),
    (18, 171),
    (0, 0),
    (227, 25878),
    (100, 5050),
    (500, 125250),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = number_sum(input1)
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