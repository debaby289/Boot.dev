"""
Assignment
When a character in Fantasy Quest is attacked, the strength of the attack is compared to the strength of the character's defensive enchantments. If the character has any enchantment that is at least as strong as the attack, then the attack is blocked and the character takes no damage.

Fix the check_defense function.

It checks each defensive enchantment against the attack. If an enchantment is strong enough, it prints that the attack is blocked. In that case, the loop should stop instead of checking further… make sure that it does!
"""

def check_defense(attack_strength, min_enchantment, max_enchantment):
    for enchantment_strength in range(min_enchantment, max_enchantment + 1):
        print(
            f"Comparing attack strength {attack_strength} to enchantment strength {enchantment_strength}."
        )

        if enchantment_strength >= attack_strength:
            print("Attack blocked!")
            break


# Don't touch below this line


def test(attack_strength, min_enchantment, max_enchantment):
    print(
        f"Testing attack strength {attack_strength} vs. enchantment strengths {min_enchantment}–{max_enchantment}:"
    )
    check_defense(attack_strength, min_enchantment, max_enchantment)
    print("========================================")


def main():
    test(5, 8, 12)
    test(8, 6, 10)
    test(10, 5, 8)
    test(7, 4, 7)


main()
