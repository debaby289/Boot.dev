"""
Your teammate wrote a function to average a list of scores that may contain junk values from a messy log. It crashes and sometimes returns the wrong result.

Fix the safe_average(values) function so it behaves as follows:

Include only real numbers: integers and floats.
Exclude booleans (True/False). Note: in Python, bool is a subtype of int, so make sure to skip them.
Ignore all other types (strings, None, lists, dicts, etc.).
If there are no valid numbers after filtering, return None (don’t raise an error).
Use a simple loop to compute the result.
"""

def safe_average(values):
    if not values:
        return None  # no input, no average

    total = 0
    count = 0
    for v in values:
        if isinstance(v, int) and not isinstance(v, bool):
            total += v
            count += 1
        elif isinstance(v, str) and v.isdigit():
            total += int(v)
            count += 1

    # if no valid numbers found, return None
    if count == 0:
        return None

    return total / count

run_cases = [
    ([10, 20, 30], 20.0),
    ([5, "N/A", 15, None], 10.0),
    ([True, 10, False, 20], 15.0),
]

submit_cases = run_cases + [
    ([], None),
    (["oops", None], None),
    ([1.0, 2, 3.0, "nope"], 2.0),
]


def test(input_values, expected_output):
    print("---------------------------------")
    print(f"Input: {input_values}")
    result = safe_average(input_values)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for case in test_cases:
        correct = test(*case)
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