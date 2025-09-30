"""
Assignment
Complete the join_strings() function. It takes a list of strings and returns a new single string. The new string is the concatenation of all the input strings from the list end-to-end, in order, with a comma between them.
"""

def join_strings(strings):
    result = strings[0]
    
    for s in strings[1:]: 
        result += "," + s
    return result

run_cases = [
    (["hello", "world"], "hello,world"),
    (["this", "list", "is", "so", "important"], "this,list,is,so,important"),
]

submit_cases = run_cases + [
    ([], ""),
    (["zuck", "satya", "cook", "bezos"], "zuck,satya,cook,bezos"),
    (["dota", "sc2", "overwatch", "diablo", "mtg"], "dota,sc2,overwatch,diablo,mtg"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print("")
    result = join_strings(input1)
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