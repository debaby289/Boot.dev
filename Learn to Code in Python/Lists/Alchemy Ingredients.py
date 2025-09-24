"""
Assignment
Complete the check_ingredient_match function. It accepts two lists of strings:

recipe: The list of ingredients needed.
ingredients: The list of ingredients the character has.
It should return two values:

A float representing the percentage of required ingredients the character has.
A new list of ingredients the character is missing but that are required.
Assume that the recipe list won't contain any duplicates (recipes require only one ingredient of each kind).
"""

def check_ingredient_match(recipe, ingredients):
    #Starting Variables
    listCount = len(recipe)
    match = 0
    missing = []
    
    #Grab the required list
    for item in recipe:
        if item in ingredients:
            match += 1
        else:
            missing.append(item)

    #Calculate the percentage of match
    percentage = (match / listCount) * 100

    #Return the percentage and missing items
    return percentage, missing

run_cases = [
    (
        [
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Elf Dust",
            "Goblin Ear",
        ],
        (50.0, ["Mandrake Root", "Griffin Feather"]),
    ),
    (
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Dragon Scale",
            "Phoenix Feather",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        (75.0, ["Unicorn Hair", "Troll Tusk"]),
    ),
]

submit_cases = run_cases + [
    (
        [
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
            "Unicorn Hair",
        ],
        [
            "Goblin Ear",
            "Elf Dust",
            "Griffin Feather",
            "Mermaid Tear",
            "Goblin Ear",
            "Phoenix Feather",
            "Troll Tusk",
            "Unicorn Hair",
        ],
        (
            75.0,
            [
                "Dragon Scale",
                "Mandrake Root",
            ],
        ),
    ),
    (
        [
            "Orc Tears",
            "Ogre Ear",
            "Goblin Giggles",
            "Witch Broom",
            "Giant Toenail Clipping",
            "Centipede Foot",
            "Dog Hair",
            "Bald Eagle Dandruff",
        ],
        [
            "Unicorn Hair",
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Griffin Feather",
            "Mandrake Root",
            "Goblin Ear",
            "Bald Eagle Dandruff",
        ],
        (
            12.5,
            [
                "Orc Tears",
                "Ogre Ear",
                "Goblin Giggles",
                "Witch Broom",
                "Giant Toenail Clipping",
                "Centipede Foot",
                "Dog Hair",
            ],
        ),
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f" - Recipe: {input1}")
    print(f" - Ingredients: {input2}")
    print("")
    result = check_ingredient_match(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result[0] == expected_output[0] and sorted(result[1]) == sorted(
        expected_output[1]
    ):
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