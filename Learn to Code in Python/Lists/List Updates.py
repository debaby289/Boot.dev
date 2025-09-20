"""
Assignment
Fantasy Quest is trialing a new inventory system for their hardcore game mode. If a player has Iron Ore or an Iron Bar, it is always stored in the 2nd inventory slot (and they can only have one or the other).

Let's finish the smelt_ore function:
    Check if they have Iron Ore in the second inventory slot.
    If they do, change it into an Iron Bar.
"""

def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory


player_inventory = ["Player", "Iron Ore", 5]
print(smelt_ore(player_inventory))

# Output: ['Player', 'Iron Bar', 5]