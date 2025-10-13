"""
Fix Drain Battery Levels
The drain_battery function should simulate a phone battery draining in steps. On each tick, reduce the charge by usage_per_tick and record the new level. The battery should never go below 0.

Expected behavior:
    Start with an initial charge (an integer >= 0) and a positive usage_per_tick.
    On each tick, subtract usage_per_tick from charge.
    If the result is below 0, use 0 instead.
    Record each post-drain level in order until the charge reaches 0.
"""

def drain_battery(charge, usage_per_tick):
    levels = []
    while charge > 0:
        charge -= usage_per_tick
        charge = max(charge, 0)   # prevent negatives
        levels.append(charge)
    return levels

run_cases = [
    ((10, 3), [7, 4, 1, 0]),
    ((5, 5), [0]),
]

submit_cases = run_cases + [
    ((1, 2), [0]),
    ((9, 4), [5, 1, 0]),
    ((0, 3), []),
    ((12, 1), [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
]


def test(input_tuple, expected_output):
    charge, usage_per_tick = input_tuple
    print("---------------------------------")
    print(f"Input charge: {charge}")
    print(f"Usage per tick: {usage_per_tick}")
    result = drain_battery(charge, usage_per_tick)
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