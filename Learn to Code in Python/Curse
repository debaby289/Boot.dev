def curse(weapon_damage):
    lesser_cursed = weapon_damage * .50
    greater_cursed = weapon_damage * .25
    return lesser_cursed,greater_cursed

# Don't modify below this line

def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")

def main():
    test(100)
    test(500)
    test(1000)

main()
