def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line
    #Simplified Version
    for item in items:
        #item = items[i]
        if item == "Potion":
            potion_count += 1
        elif item == "Bread":
            bread_count += 1
        elif item == "Shortsword":
            shortsword_count += 1
    
    '''
    Complex Version
    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1
        else:
            pass
    '''

    # don't touch below this line

    return potion_count, bread_count, shortsword_count

