def is_eligible_driver(age, has_permit):
    if age >= 16 and has_permit == True:
        return True
    else:
        return False

def within_safe_temp(temp):
    if 68 <= temp <= 77:
        return True
    else:
        return False

def better_score(a, b):
    if a > b:
        return "A"
    elif a < b:
        return "B"
    else:
        return "Tie"
