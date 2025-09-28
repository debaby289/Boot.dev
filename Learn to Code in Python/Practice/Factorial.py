"""
Assignment
Complete the factorial() function. It should return the factorial of a given number.
"""

def factorial(num):
    if num == 0:
        return 1
    
    result = 1
    for n in range(1, num + 1):
        result *= n  # 
    return result

run_cases = [
    (0, 1),
    (4, 24),
]

submit_cases = run_cases + [
    (1, 1),
    (5, 120),
    (7, 5040),
    (9, 362880),
    (13, 6227020800),
    (15, 1307674368000),
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print("")
    result = factorial(input)
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
            print("Pass")
            passed += 1
        else:
            print("Fail")
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