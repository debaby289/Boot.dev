"""
Assignment
Complete the check_high_score function. 
If the player_name matches the high score name, return the string:
high
Otherwise, if it's the low scorer, return the string:
low
Otherwise, return the string:
neither
"""

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
    
run_cases = [
    ("ash ketchum", "ash ketchum", "You are the highest scoring player!"),
    ("brock", "ash ketchum", "You are not the highest scoring player!"),
]

submit_cases = run_cases + [
    ("misty", "brock", "You are not the highest scoring player!"),
    ("", "", "You are the highest scoring player!"),
    ("same", "same", "You are the highest scoring player!"),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = check_high_score(input1, input2)
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
