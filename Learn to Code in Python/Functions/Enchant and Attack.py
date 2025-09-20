"""
Assignment
Complete the enchant_and_attack function. It creates a new "enchanted" name for a weapon and calculates how much damage the enchanted weapon will deal to a targeted enemy.

It accepts 3 parameters:
    target_health: integer
    damage: integer
    weapon: string

It should do the following things in the function body:

Calculate and store the "enchanted damage" in a new variable. The enchanted damage should be the input damage plus 10.
Calculate and store the "new health" in a new variable. The new health should be the input target_health minus the enchanted damage.
Create a new variable called enchanted_weapon. It should be the input weapon with the string "enchanted " added to the beginning of it. For example:
    sword -> enchanted sword
    axe -> enchanted axe
Return the enchanted weapon and the new health in that order.
"""

def enchant_and_attack(target_health, damage, weapon):
    ed = damage + 10
    new_health = target_health - ed
    enchanted_weapon = f"enchanted {weapon}"
    return enchanted_weapon, new_health

# Don't modify below this line

def test(target_health, damage, weapon):
    print(f"The target has {target_health} health.")
    print(f"{weapon} base damage: {damage}... Enchanting and attacking.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"The target has been attacked with the {enchanted_weapon}.")
    print(f"The target has {new_health} health remaining.")
    print("=====================================")

def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()
