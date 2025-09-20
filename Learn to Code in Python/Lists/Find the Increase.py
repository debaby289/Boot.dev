"""
Assignment
Every day, character levels are recorded in a list. When someone levels up, we congratulate them! Your assignment is to compare the levels to identify which characters need to be congratulated!

Complete the loop inside check_character_levels. It already loops over all of the indexes i in old_character_levels. The old_character_levels and new_character_levels lists are the same length, which means you can use i to index into both.

    For each iteration, use i with bracket notation to get the items at the same index from both lists.
    Check if the level in old_character_levels is less than the level in the new_character_levels.
    If so, print i. (Do not print anything if they didn't level up or somehow leveled down.)
"""

def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] < new_character_levels[i]:
            print(i)

# don't touch below this line

def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")

def main():
    test()

main()
