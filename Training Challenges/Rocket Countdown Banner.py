"""
It should return a two-line string:
    First line: a space-separated countdown from n down to 1
    Second line: exactly n asterisks (*)
No extra spaces at the start or end of the first line.
"""

def rocket_banner(n):
    countdown = ""
    i = n
    while i >= 1:
        if countdown:
            countdown += " "
        countdown += str(i)
        i -= 1

    stars = ""
    for _ in range(n):
        stars += "*"

    return countdown + "\n" + stars

run_cases = [
    (3, "3 2 1\n***"),
    (6, "6 5 4 3 2 1\n******"),
]

submit_cases = run_cases + [
    (1, "1\n*"),
    (2, "2 1\n**"),
    (10, "10 9 8 7 6 5 4 3 2 1\n**********"),
]


def test(n, expected_output):
    print("---------------------------------")
    print(f"Input n: {n}")
    result = rocket_banner(n)
    print("Expected:\n" + expected_output)
    print("Actual:\n" + result)
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


# Default to submit cases, use run cases for quicker feedback when supported
test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()