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
