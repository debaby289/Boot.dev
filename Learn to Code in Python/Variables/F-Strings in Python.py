"""
Assignment
Fix the bug on line 7. Use an f-string to inject the dynamic values into the string:

Replace NAME with the value of the name variable
Replace RACE with the value of the race variable
Replace AGE with the value of the age variable
Do not "hard-code" the values into the string. For example, this is not the solution we're looking for (even though it happens to work in this case):
"""

name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")
