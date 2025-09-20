"""
Fix Your First Bug
The combat system in Fantasy Quest isn't working as intended! It appears that players are gaining health when attacked instead of losing it.

Assignment
Fix the math bug on line 3.
"""
sword_damage = 10
start_health = 100
end_health = start_health - sword_damage
#Error: end_health = start_health + sword_damage

# Don't touch below this line
print(f"Sam's health is: {start_health}")
print(f"Sam takes {sword_damage} damage...")
print(f"Sam's health is: {end_health}")
