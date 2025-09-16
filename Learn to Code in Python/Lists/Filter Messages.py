def filter_messages(messages):
    #Empty Lists
    filterMsg = []
    counts = []
    #Outer Loop
    for msg in messages:
        words = msg.split()
        gWords = []
        dang_count = 0
        #Inner loop
        for word in words:
            #Conditional
            if word == "dang":
                dang_count += 1
            else:
                gWords.append(word)
        #Rejoin messages    
        filtered = " ".join(gWords)
        filterMsg.append(filtered)
        counts.append(dang_count)
    return filterMsg, counts