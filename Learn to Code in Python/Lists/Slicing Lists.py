def get_champion_slices(champions):
    list1 = champions[2:]
    list2 = champions[:-1]
    list3 = champions[::2]
    champions = list1,list2,list3
    return champions  

    #Simple Option
    #return champions[2:], champions[:-1], champions[::2]
