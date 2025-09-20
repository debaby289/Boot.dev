"""
Assignment
Our players need a way to see how many copies of a specific item they have within their inventory!

Let's finish the get_item_counts function.

Within the loop, check if the items are a Potion, Bread, or Shortsword.
If you find a match, increment the corresponding counter, either potion_count, bread_count or shortsword_count.
"""

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line
    #Simplified Version
    for item in items:
        #item = items[i]
        if item == "Potion":
            potion_count += 1
        elif item == "Bread":
            bread_count += 1
        elif item == "Shortsword":
            shortsword_count += 1

    # don't touch below this line

    return potion_count, bread_count, shortsword_count

run_cases = [
    (["Bread", "Potion", "Shortsword", "Bread"], (1, 2, 1)),
    (["Potion", "Potion", "Shortsword", "Buckler", "Iron Mace"], (2, 0, 1)),
]

submit_cases = run_cases + [
    ([], (0, 0, 0)),
    (
        [
            "Potion",
            "Leather Scraps",
            "Bread",
            "Iron Ore",
            "Light Leather",
            "Bread",
            "Shortsword",
            "Longsword",
            "Ironwood Branch",
            "Shortsword",
            "Shortsword",
        ],
        (1, 2, 3),
    ),
    (["Bread", "Bread", "Bread", "Bread"], (0, 4, 0)),
    (["Shortsword", "Shortsword", "Shortsword", "Shortsword"], (0, 0, 4)),
    (["Potion"], (1, 0, 0)),
    (["Potion", "Bread", "Shortsword"], (1, 1, 1)),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    result = get_item_counts(input)
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