"""
Assignment
In Fantasy Quest there is a list of strongholds on the map that players can visit to defeat powerful bosses. Let's update the trim_strongholds function to:

Delete the first stronghold from the list
Delete the last two strongholds from the list
"""

def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]

run_cases = [
    (
        [
            "Rivendale",
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
            "Mordane",
            "Gondolin",
        ],
        [
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
        ],
    ),
]

submit_cases = run_cases + [
    (
        [
            "Pogsmeade",
            "Dogwarts",
            "The Leaky Pot",
            "The Screaming Hut",
        ],
        [
            "Dogwarts",
        ],
    ),
    (
        [
            "Midgard",
            "Cosmo Canyon",
            "Nibelheim",
            "Costa del Sol",
            "Pallet Town",
            "Viridian City",
            "Salamandastron",
            "Redwall Abbey",
            "Fisherman's Horizon",
            "Waterdeep",
            "Elturel",
            "Candlekeep",
            "Chult",
            "Eorzea",
            "Ratchet",
            "Orgrimmar",
            "Stormwind",
            "Shattrath",
            "Dalaran",
        ],
        [
            "Cosmo Canyon",
            "Nibelheim",
            "Costa del Sol",
            "Pallet Town",
            "Viridian City",
            "Salamandastron",
            "Redwall Abbey",
            "Fisherman's Horizon",
            "Waterdeep",
            "Elturel",
            "Candlekeep",
            "Chult",
            "Eorzea",
            "Ratchet",
            "Orgrimmar",
            "Stormwind",
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"    Input: {input1}")
    trim_strongholds(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {input1}")
    if input1 == expected_output:
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