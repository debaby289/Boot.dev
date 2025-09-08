def meditate(mana, max_mana, num_potions):
    while (num_potions > 0) and (mana != max_mana):
        mana += 1
        num_potions -= 1
    return mana,num_potions
