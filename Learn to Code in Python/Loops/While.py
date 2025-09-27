"""
Assignment
In Fantasy Quest, player characters regenerate health when standing still while away from enemies. This means they will gain health but can't run from enemies that are coming towards them while regenerating.

Complete the regenerate function using a while loop. It takes current_health, max_health and enemy_distance integers and returns an integer.

Use a while loop to determine if they can regenerate. Assume they're stationary and enemies are pursuing them. The character can regenerate while both of these conditions are true:
    The character's current_health is less than their max_health.
    An enemy is more than a distance of 3 from the character.
For each iteration of the loop:
    The character gains 1 health.
    The enemy_distance shortens by 2.
Return the new current_health after regeneration stops.
"""

def regenerate(current_health, max_health, enemy_distance):
    while (current_health < max_health) and (enemy_distance > 3):
        current_health += 1
        enemy_distance -= 2
    return current_health

run_cases = [(0, 10, 20, 9), (0, 10, 4, 1), (8, 10, 20, 10)]

submit_cases = run_cases + [
    (0, 0, 0, 0),
    (9, 10, 3, 9),
    (100, 100, 200, 100),
    (2, 110, 50, 26),
    (100, 1010, 2000, 1010),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f" * current_health: {input1}")
    print(f" *     max_health: {input2}")
    print(f" * enemy_distance: {input3}")
    print(f"Expected Health: {expected_output}")
    result = regenerate(input1, input2, input3)
    print(f"  Actual Health: {result}")
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
