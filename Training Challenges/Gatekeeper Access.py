"""
Complete the gate_decision(level, reputation, has_key) function.

Given a player's stats, decide if they can enter a restricted area. Use comparisons and basic boolean logic.

Return exactly one of these strings:

"Enter: Keyholder"
"Enter: Veteran"
"Wait"
"Denied"
Rules (checked in this order):

If the player has the key AND their level is 5 or higher → "Enter: Keyholder"
Else if their level is 10 or higher AND their reputation is 100 or higher → "Enter: Veteran"
Else if their level is 7 or higher OR their reputation is 70 or higher → "Wait"
Else → "Denied"
Notes:

has_key is a boolean (True or False).
Use comparison operators like >= and boolean operators like and/or.
"""

def gate_decision(level, reputation, has_key):
    if has_key == True and level >= 5: 
        return "Enter: Keyholder"
    elif level >= 10 and  reputation >= 100:
        return "Enter: Veteran"
    elif level >= 7 or reputation >= 70:
        return "Wait"
    else:
        return "Denied"


run_cases = [
    (5, 20, True, "Enter: Keyholder"),
    (9, 65, False, "Wait"),
    (12, 120, False, "Enter: Veteran"),
]

submit_cases = run_cases + [
    (1, 0, False, "Denied"),
    (4, 80, True, "Wait"),
    (15, 30, True, "Enter: Keyholder"),
]


def test(level, reputation, has_key, expected_output):
    print("---------------------------------")
    print("Input:")
    print(f"  level:      {level}")
    print(f"  reputation: {reputation}")
    print(f"  has_key:    {has_key}")
    result = gate_decision(level, reputation, has_key)
    print("")
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