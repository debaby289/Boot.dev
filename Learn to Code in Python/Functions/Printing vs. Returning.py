"""
Assignment
There's a problem in the get_title function! It's supposed to construct the title value and return it to the caller. Instead, it's barbarically printing the value to the console.

Fix the function so that it returns the title instead of printing it to the console.
"""
def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return(title)

# Don't touch below this line

def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")

test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")
