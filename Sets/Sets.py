"""
Assignment
Complete the remove_duplicates function. It should take a list of spells that a player has learned and return a new List where there is at most one of each title. You can accomplish this in at least two ways:

Iteration:
    Create a set to track spells that have been seen
    Create a list to store the unique spells
    Iterate over the list
    If the spell is not in the set, add it to the set and the list
    Return the list
    Set conversion:

Convert the list to a set
    Convert the set back to a list and return it.
    It makes no sense to learn a spell twice! Once it's learned, it's learned forever.
"""

def remove_duplicates(spells):

    #Empty set and list
    track_spells = set()
    unique_spells = {}

    #Check if list is empty
    if spells == []:
        unique_spells = spells
    else:
        for spell in spells:
            track_spells.add(spell)
            unique_spells = list(track_spells)
    return unique_spells
    
    run_cases = [
    (
        [
            "fireball",
            "eldritch blast",
            "fireball",
            "eldritch blast",
            "chill touch",
            "eldritch blast",
            "chill touch",
            "chill touch",
            "fireball",
            "fireball",
            "shocking grasp",
            "fireball",
            "fireball",
        ],
        ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
    )
]

submit_cases = run_cases + [
    (["fireball", "fireball", "fireball"], ["fireball"]),
    (
        ["fireball", "eldritch blast", "chill touch", "shocking grasp"],
        ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
    ),
    (["chill touch", "chill touch", "chill touch"], ["chill touch"]),
    (["shocking grasp", "shocking grasp", "shocking grasp"], ["shocking grasp"]),
    ([], []),
    (["eldritch blast", "eldritch blast", "eldritch blast"], ["eldritch blast"]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * spells: {input}")
    print(f"Expected:  {expected_output}")
    result = remove_duplicates(input)
    print(f"   Actual: {result}")
    if not isinstance(result, list):
        print("Fail: result is not a list")
        return False
    result.sort()
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
