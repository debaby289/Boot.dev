"""
Assignment
Complete the split_players_into_teams function.

It accepts a list of players (strings representing their names) and returns two lists in this order:
    A new list of all the players with even-numbered indexes in the original list.
    A new list of all the players with odd-numbered indexes in the original list.
Use a slice with a "step" to create two new lists from the players list. Don't be afraid to consult your spellbook for list slicing help!
"""

def split_players_into_teams(players):
    return players[::2], players[1::2]

run_cases = [
    (
        [
            "Harry",
            "Hermione",
            "Ron",
            "Ginny",
            "Fred",
            "Neville",
            "Draco",
            "Luna",
            "Cho",
            "Gregory",
            "Lee",
            "Michael",
            "Lavender",
            "Frank",
            "Anthony",
            "Allan",
        ],
        (
            ["Harry", "Ron", "Fred", "Draco", "Cho", "Lee", "Lavender", "Anthony"],
            [
                "Hermione",
                "Ginny",
                "Neville",
                "Luna",
                "Gregory",
                "Michael",
                "Frank",
                "Allan",
            ],
        ),
    ),
    (["Mike", "Walter", "Skyler", "Tuco"], (["Mike", "Skyler"], ["Walter", "Tuco"])),
]

submit_cases = run_cases + [
    (["Alice", "Bob", "Charlie", "David"], (["Alice", "Charlie"], ["Bob", "David"])),
    ([], ([], [])),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = split_players_into_teams(input1)
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