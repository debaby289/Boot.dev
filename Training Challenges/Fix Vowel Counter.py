def count_vowels(text):
    count = 0
    for ch in text:
        # Bug: this condition is always true for non-empty strings
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
            count += 1
    return count

run_cases = [
    ("Boot.dev", 3),
    ("Hello there", 4),
    ("PYTHON", 1),
]

submit_cases = run_cases + [
    ("", 0),
    ("bcdfg", 0),
    ("aeiouAEIOU", 10),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    result = count_vowels(input1)
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