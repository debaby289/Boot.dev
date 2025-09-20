""""
Assignment
When our hero walks through poison, their health should go down. Right now the hero is gaining 10 health instead of losing 10 health. Change the poison_damage variable to be negative.
"""

player_health = 100
poison_damage = -10

# don't touch below this line

player_poison_health = player_health + poison_damage

print(player_poison_health)
