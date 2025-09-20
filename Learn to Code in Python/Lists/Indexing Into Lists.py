"""
Assignment
We need to allow our players to access items in their inventories!

Fix our get_leather_scraps function by changing the value of item_index to the index in inventory that holds the value "Leather Scraps".
"""

def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]
