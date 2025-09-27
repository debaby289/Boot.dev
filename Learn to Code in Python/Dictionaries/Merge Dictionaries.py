"""
Assignment
Complete the merge function. It accepts two dictionaries as input and returns a new merged dictionary that contains all the keys and values from the input dictionaries.

There are multiple solutions that use built-in Python functions, but we'll use loops for practice:
    Create an empty dictionary to hold the new merged result
    Iterate over the key/value pairs of dict1 and add them to the merged dictionary
    Iterate over the key/value pairs of dict2 and add them to the merged dictionary
    Return the newly merged dictionary
"""

def merge(dict1, dict2):
    #Empty
    merged_dict = {}

    #For loops
    for key in dict1:
        merged_dict[key] = dict1[key]
    
    #For loops
    for key in dict2:
        merged_dict[key] = dict2[key]

    #Return Value
    return merged_dict

run_cases = [
    (
        {"Goku": 8000, "Vegeta": 7500},
        {"Piccolo": 3500, "Gohan": 2800},
        {
            "Goku": 8000,
            "Vegeta": 7500,
            "Piccolo": 3500,
            "Gohan": 2800,
        },
    ),
    (
        {"Frieza": 120000, "Cell": 900000},
        {"Majin_Buu": 1100000, "Broly": 10000},
        {
            "Frieza": 120000,
            "Cell": 900000,
            "Majin_Buu": 1100000,
            "Broly": 10000,
        },
    ),
]

submit_cases = run_cases + [
    ({}, {}, {}),
    (
        {
            "Android_17": 30000,
            "Android_18": 30000,
            "Future_Trunks": 9000,
            "Kid_Trunks": 7000,
        },
        {
            "Android_17": 40000,
            "Dr_Gero": 10000,
            "Goten": 6500,
            "Future_Gohan": 8000,
        },
        {
            "Android_17": 40000,
            "Android_18": 30000,
            "Dr_Gero": 10000,
            "Future_Trunks": 9000,
            "Kid_Trunks": 7000,
            "Goten": 6500,
            "Future_Gohan": 8000,
        },
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * first_half:  {input1}")
    print(f" * second_half: {input2}")
    result = merge(input1, input2)
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