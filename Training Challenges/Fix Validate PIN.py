"""
Fix Validate PIN
The validate_pin function should return True only if the input is a string of digits with a length of exactly 4 or exactly 6. Otherwise, it should return False.

Right now it's incorrectly accepting some invalid PINs (like those with letters or the wrong length).

Expected behavior:

Accept only digits 0-9
Length must be 4 or 6
No spaces or symbols
"""

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for ch in pin:
            if not ch.isdigit():
                return False
        return True
    return False

run_cases = [
    ("1234", True),
    ("a234", False),
    ("123456", True),
]

submit_cases = run_cases + [
    ("12345", False),
    ("1234567", False),
    ("12 34", False),
    ("0000", True),
    ("098765", True),
    ("", False),
    ("123\n", False),
    ("-1234", False),
    ("1234 ", False),
    ("999999", True),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {repr(input1)}")
    result = validate_pin(input1)
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
