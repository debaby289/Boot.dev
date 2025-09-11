########################################################################################
#Written by me
########################################################################################
def unique_playlist(songs):
    result = []
    for song in songs:
        if song not in result:
            result.append(song)
    return result

########################################################################################
#Written by Boot.dev
########################################################################################
run_cases = [
    (["Intro", "Beat It", "Intro", "Finale", "Beat It"], ["Intro", "Beat It", "Finale"]),
    (["A", "B", "C"], ["A", "B", "C"]),
    ([], []),
]

submit_cases = run_cases + [
    (["loop", "loop", "loop", "loop"], ["loop"]),
    (["a", "A", "a", "A"], ["a", "A"]),
    ([1, 2, 1, 3, 2, 4, 4, 5], [1, 2, 3, 4, 5]),
    (["x", "y", "z", "x", "y"], ["x", "y", "z"]),
]

def test(input_list, expected_output):
    print("---------------------------------")
    print(f"Input playlist: {input_list}")
    result = unique_playlist(input_list)
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