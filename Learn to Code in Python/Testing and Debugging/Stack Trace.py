"""
Assignment
Go ahead and run the code in its current state. You should see something like this:

PythonError: Traceback (most recent call last):
  File "<exec>", line 17, in <module>
  File "<string>", line 1, in <module>
  File "/home/pyodide/main.py", line 3
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
                                                                                                                  ^
IndentationError: unindent does not match any outer indentation level

PythonError: Traceback (most recent call last):
This is a standard header that's just letting us know that a Python traceback is what we're looking at.

File "<exec>", line 17, in <module> and File "<string>", line 1, in <module>
This is the start of the "trace". These strange "<exec>" and "<string>" files don't really exist, the Python interpreter is letting us know about them because they have to do with how your code is executed in a virtual browser-based environment.

File "/home/pyodide/main.py", line 3
Now we're getting to the real meat of the error message! The purpose of a "trace" is to show us the path that the Python interpreter took through our code before it encountered the error, which can help us figure out what went wrong.

In this case, the interpreter was executing the code in the main.py file, and it got to line 3 before it encountered the error.

msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
This is the line of code that caused the error.

IndentationError: unindent does not match any outer indentation level
This is the type of error that was raised. In this case, it's an IndentationError, which means that the Python interpreter was expecting a certain amount of indentation (whitespace at the beginning of the line) but it didn't get what it was expecting.

Don't be fooled! The proper amount of indentation in Python is 4 spaces (or one <tab> stroke). In this case, line 2 is actually indented 6 spaces, which is why the interpreter is confused. Fix line 2.

Run the code again. You should see another error, this time the last few lines are something like:

msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
                                                                                                 ^
SyntaxError: unterminated string literal (detected at line 3)

Now we have a SyntaxError, which is just a more general type of error related to invalid code. Take a close look at line 3 and fix the problem.
"""

def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg
