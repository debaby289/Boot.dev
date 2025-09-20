"""
Assignment
In Fantasy Quest, we want to grant the player an enchantment for every third quest that they complete. And the higher the number of quests completed, the stronger the enchantment.

Fix the award_enchantments function. It calculates the strength of the enchantment – 5 times the number of quests completed – and prints a message for the player. But we need to make sure this happens only once every 3 quests!

At the beginning of the function, before the loop, initialize a counter variable to 0.
Within the for loop:
    Add 1 to counter in each iteration, to keep track of how many quests we've seen.
    If counter is less than 3, continue to the next iteration.
    Otherwise, we must have completed 3 quests! Reset counter to 0 before the enchantment is awarded.
"""

def award_enchantments(start, end, step):
    for quest_number in range(start, end, step):
        if quest_number % 3 == 0:
            enchantment_strength = quest_number * 5
            print (
                f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
            )

# Don't touch below this line

def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")

def main():
    test(1, 11, 1)
    test(20, 24, 1)
    test(10, 12, 1)
    test(11, 19, 1)

main()