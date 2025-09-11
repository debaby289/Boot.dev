def rocket_banner(n):
    countdown = ""
    i = n
    while i >= 1:
        if countdown:
            countdown += " "
        countdown += str(i)
        i -= 1

    stars = ""
    for _ in range(n):
        stars += "*"

    return countdown + "\n" + stars