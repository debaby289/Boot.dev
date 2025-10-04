"""
Fix Parse and Divide
The parse_and_divide function should:
    Convert two input strings into integers.
    Return the integer result of dividing the first number by the second using whole-number division.
    If either string can't be converted to an integer, return "Invalid number".
    If the second number is 0, return "Cannot divide by zero".
Right now the function mixes up the error messages and returns the wrong type for successful division
"""

def parse_and_divide(numerator_str, denominator_str):
    try:
        result = int(numerator_str) // int(denominator_str)
        return result
    except ValueError:
            return "Invalid number"
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
run_cases = [
    ("10", "2", 5),
    ("-9", "-3", 3),
    ("0", "5", 0),
]

submit_cases = run_cases + [
    ("7", "1", 7),
    ("100", "10", 10),
    ("abc", "5", "Invalid number"),
    ("12", "xyz", "Invalid number"),
    ("42", "0", "Cannot divide by zero"),
    ("-12", "3", -4),
    ("81", "9", 9),
]


def test(numerator_str, denominator_str, expected_output):
    print("---------------------------------")
    print(f"Input numerator:   {numerator_str}")
    print(f"Input denominator: {denominator_str}")
    result = parse_and_divide(numerator_str, denominator_str)
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