"""
Assignment
Complete the count_vowels function. It takes a string and returns:
    The number of vowels in the string
    A set of the unique vowels found in the string
We are only interested in the 5 vowels: a, e, i, o, u, and their capitalized versions. Treat uppercase and lowercase vowels as separate. For example, "A" and "a" are not the same.
"""

def count_vowels(text):
    #Vowel Variable
    vowel_count = 0
    #set for vowels
    vowel_list = set()

    for letter in text:
        if letter in {"a","e","i","o","u","A","E","I","O","U"}:
            vowel_count += 1
            vowel_list.add(letter)
    return vowel_count, vowel_list
            
run_cases = [
    (
        "Did someone say Thunderfury, Blessed Blade of the Windseeker?",
        (19, {"u", "o", "i", "e", "a"}),
    ),
    ("LF9M UBRS NEED ALL!!!!", (4, {"U", "E", "A"})),
]

submit_cases = run_cases + [
    ("Leatherworker LFW Have all end game recipes!", (14, {"e", "i", "o", "a"})),
    ("", (0, set())),
    (
        "Can anyone spare 1g so I can train my new spells?",
        (13, {"o", "I", "i", "e", "a"}),
    ),
    ("no", (1, {"o"})),
    ("mages need a nerf", (6, {"e", "a"})),
    ("wtb port to Roshar", (4, {"o", "a"})),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Text: {input1}")
    print(f"Expected: {expected_output}")
    result = count_vowels(input1)
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