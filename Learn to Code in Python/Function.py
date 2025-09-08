def to_celsius(f):
    f_to_c_temp = 5/9 * (f - 32)
    return f_to_c_temp

## Don't touch below this line

def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)
