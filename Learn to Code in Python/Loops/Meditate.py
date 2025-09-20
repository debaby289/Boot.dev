"""
Assignment
Complete the meditate function using a while loop. It accepts:

    mana: the current mana of the character.
    max_mana: the maximum mana of the character.
    num_potions: the number of mana potions the character has.

It consumes potions one at a time until either:

    The character's mana has reached its maximum
    The character has no more potions left
    
Each potion restores 1 point of mana.

When the meditation is over, it returns the player's mana and the number of potions left, in that order.
"""

def meditate(mana, max_mana, num_potions):
    while (num_potions > 0) and (mana != max_mana):
        mana += 1
        num_potions -= 1
    return mana,num_potions
