def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory


player_inventory = ["Player", "Iron Ore", 5]
print(smelt_ore(player_inventory))

# Output: ['Player', 'Iron Bar', 5]