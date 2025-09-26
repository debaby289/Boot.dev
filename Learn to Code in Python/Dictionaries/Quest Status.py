"""
Assignment
Complete the get_quest_status function. It accepts a progress dictionary (structure defined above) and returns the character's status in the "bridge_run" quest.
"""

def get_quest_status(progress):
    return progress["entity"]["character"]["quests"]["bridge_run"]["status"]

run_cases = [
    (
        {
            "entity": {
                "character": {
                    "name": "Sir Galahad",
                    "quests": {
                        "bridge_run": {
                            "status": "In Progress",
                        },
                        "talk_to_syl": {
                            "status": "Completed",
                        },
                    },
                }
            }
        },
        "In Progress",
    ),
    (
        {
            "entity": {
                "character": {
                    "name": "Lady Gwen",
                    "quests": {
                        "bridge_run": {
                            "status": "Completed",
                        },
                        "talk_to_syl": {
                            "status": "In Progress",
                        },
                    },
                }
            }
        },
        "Completed",
    ),
]

submit_cases = run_cases + [
    (
        {
            "entity": {
                "character": {
                    "name": "Archer Finn",
                    "quests": {
                        "bridge_run": {
                            "status": "Not Started",
                        },
                        "talk_to_syl": {
                            "status": "Completed",
                        },
                    },
                }
            }
        },
        "Not Started",
    ),
    (
        {
            "entity": {
                "character": {
                    "name": "Mage Elara",
                    "quests": {
                        "bridge_run": {
                            "status": "Failed",
                        },
                        "talk_to_syl": {
                            "status": "Completed",
                        },
                    },
                }
            }
        },
        "Failed",
    ),
    (
        {
            "entity": {
                "character": {
                    "name": "Rogue Talon",
                    "quests": {
                        "bridge_run": {
                            "status": "Completed",
                        },
                        "talk_to_syl": {
                            "status": "Not Started",
                        },
                    },
                }
            }
        },
        "Completed",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Progress Dictionary: {input1}")
    print(f"Expected: {expected_output}")
    result = get_quest_status(input1)
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