"""
Fix Receipt Printing
Our point-of-sale script is supposed to print a simple receipt, but it won’t run because of invalid Python syntax.

Fix the code so it prints three lines, in order, using the provided variables:

Item 1 in the format: Item: Bread - Price: 3
Item 2 in the format: Item: Milk - Price: 2
Item 3 in the format: Item: Eggs - Price: 5
What to do:

Resolve the syntax mistakes so the program runs
Use the given variables to build each line
Print exactly the three receipt lines, nothing else
"""

item1 = "Bread"
price1 = "3"

item2 = "Milk"
price2 = "2"

item3 = "Eggs"
price3 = "5"

prefix = "Item: "
middle = " - Price: "

print(prefix + item1 + middle + price1)
print(prefix + item2 + middle + price2)
print(prefix + item3 + middle + price3)