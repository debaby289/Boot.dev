"""
Assignment
Complete the purchase_item function.
    If the character doesn't have enough gold raise an Exception with the text not enough gold.
    Otherwise, return the amount of remaining money the customer has after completing the purchase.
"""

def purchase_item(price, gold_available):
    #Varible Set
    value =  gold_available - price

    #Checking to see if value is negative
    if value < 0:
        raise Exception("not enough gold")
        
    
    #Retuning value if positive
    return value

run_cases = [
    (10.00, 20.00, 10.00),
    (30.00, 20.00, None, "not enough gold"),
]

submit_cases = run_cases + [
    (15.10, 15.10, 0.00),
    (1430.00, 69.00, None, "not enough gold"),
    (7.50, 7.50, 0.00),
    (100.00, 99.99, None, "not enough gold"),
    (0.00, 0.00, 0.00),
]


def test(price, gold_available, expected_output, expected_err=None):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * price: {price:.2f}")
    print(f" * gold_available: {gold_available:.2f}")
    try:
        result = purchase_item(price, gold_available)
        if result == expected_output:
            print(f"Expected: {expected_output:.2f}")
            print(f"  Actual: {result:.2f}")
            print("Pass")
            return True
    except Exception as e:
        print(f"Expected Exception: {expected_err}")
        print(f"  Actual Exception: {str(e)}")
        if str(e) == expected_err:
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