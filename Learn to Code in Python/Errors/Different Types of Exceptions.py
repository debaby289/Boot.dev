"""
Assignment
Take a look at the get_player_record function. It raises an exception for negative player_ids.

Complete the process_player_record() function so that it:
    Calls get_player_record(player_id) and returns its result if no error occurs.
    If an IndexError is raised, returns the string: index is too high.
    If any other exception happens, returns the error object itself.
"""

def process_player_record(player_id):
    try:
        value = get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e

    return value

# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]

run_cases = [
    (0, {"name": "Slayer", "level": 128}),
    (1, {"name": "Dorgoth", "level": 300}),
    (3, "index is too high"),
    (-1, "negative ids not allowed"),
]

submit_cases = run_cases + [
    (2, {"name": "Saruman", "level": 4000}),
    (10, "index is too high"),
    (-5, "negative ids not allowed"),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    result = process_player_record(input)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if isinstance(result, Exception):
        result = f"{result}"
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
