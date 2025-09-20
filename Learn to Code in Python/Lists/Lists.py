"""
Assignment
Let's work on Fantasy Quest's inventory! We can store items the player is carrying in a list!

Fix our get_inventory function by adding Shortsword to the end of the list.
"""

def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet","Shortsword"]

# Don't edit below this line

def test():
    inventory = get_inventory()
    print(f"Inventory contains: {inventory}")
    print("=====================================")

def main():
    test()

main()
