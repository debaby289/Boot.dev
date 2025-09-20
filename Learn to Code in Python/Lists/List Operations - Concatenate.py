""""
Assignment
Fantasy Quest allows users to keep lists of their favorite items. Your job is to finish the concatenate_favorites function. It takes three different lists - the player's favorite_weapons, favorite_armor and favorite_items.

Create a new list that combines the lists favorite_weapons, favorite_armor, and favorite_items in this order.
Return the list containing the combined favorites.
"""

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    newlists = favorite_weapons + favorite_armor + favorite_items
    return newlists

run_cases = [
    (
        ["sword", "dagger"],
        ["bracers", "helmet"],
        ["feather", "iron bars"],
        (["sword", "dagger", "bracers", "helmet", "feather", "iron bars"]),
    ),
]

submit_cases = run_cases + [
    (
        ["lance"],
        ["shield"],
        ["potions"],
        (["lance", "shield", "potions"]),
    ),
    (
        ["bow", "staff"],
        ["breastplate"],
        ["scrolls", "bedroll"],
        (["bow", "staff", "breastplate", "scrolls", "bedroll"]),
    ),
    ([], [], [], ([])),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    result = concatenate_favorites(input1, input2, input3)
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