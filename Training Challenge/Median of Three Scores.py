def min_of_three(a, b, c):
    if (a >= b) and (b <= c):
        return b
    elif (b >= c) and (c <= a):
        return c
    elif (c >= a) and (a <= b):
        return a
        
def median_of_three(a, b, c):
    # Max --- Min
    if ((a <= b) or (a <= c)) and ((a >= b) or (a >= c)):
        return a
    elif ((b <= a) or (b <= c)) and ((b >= a) or (b >= c)):
        return b
    elif ((c <= b) or (c <= a)) and ((c >= b) or (c >= a)):
        return c

def max_of_three(a, b, c):
    if a >= b:
        return a
    elif b >= c:
        return b
    elif c >= a:
        return c