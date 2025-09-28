"""
Assignment
Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:
{
  "height": 5,
  "width": 6
}
It should calculate the area of each rectangle and return the sum of all the areas.
"""

def area_sum(rectangles):
    #sum of all dictonaries 
    areas = 0

    #find the area of each dictonary
    for rectangle in range(0,len(rectangles)):
        area = rectangles[rectangle]['height'] * rectangles[rectangle]['width']
        areas += area
    #return the sum of all area
    return areas

run_cases = [
    ([{"height": 4, "width": 5}], 20),
    ([{"height": 4, "width": 5}, {"height": 4, "width": 9}], 56),
    ([{"height": 4, "width": 5}, {"height": 18, "width": 5}], 110),
]

submit_cases = run_cases + [
    ([{"height": 2, "width": 3}, {"height": 4, "width": 5}], 26),
    ([{"height": 6, "width": 7}, {"height": 8, "width": 9}], 114),
    ([{"height": 10, "width": 11}, {"height": 12, "width": 13}], 266),
    ([{"height": 0, "width": 0}], 0),
    ([], 0),
]


def test(input1, expected_output):
    print("---------------------------------")
    print("Input:")
    for rect in input1:
        print(f" - {rect}")
    print("")
    result = area_sum(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
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