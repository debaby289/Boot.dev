""""
Cafe Order Summary
Use the provided variables to build a short order summary for a cafe.

Compute new variables using only the given values, then print the results in order.

What to do:
Create these variables using arithmetic with the provided prices and quantities:
    coffee_total_cents
    sandwich_total_cents
    grand_total_cents (sum of the two totals)
Print exactly four lines, in this order:
    The order message by combining message_start, customer_name, and message_end
    label_coffee followed by the value of coffee_total_cents
    label_sandwich followed by the value of sandwich_total_cents
    label_grand followed by the value of grand_total_cents

Expected behavior example (structure only):
    Line 1: Order for: Ada ready
    Line 2: Coffee total (cents): 600
    Line 3: Sandwich total (cents): 750
    Line 4: Grand total (cents): 1350
"""

message_start = "Order for: "
message_end = " ready"
customer_name = "Ada"

coffee_price_cents = 300
coffee_qty = 2
sandwich_price_cents = 750
sandwich_qty = 1

label_coffee = "Coffee total (cents):"
label_sandwich = "Sandwich total (cents):"
label_grand = "Grand total (cents):"

coffee_total_cents = coffee_price_cents * coffee_qty
sandwich_total_cents = sandwich_price_cents * sandwich_qty 
grand_total_cents = coffee_total_cents + sandwich_total_cents

print(message_start + customer_name + message_end)
print(f"{label_coffee} {coffee_total_cents}")
print(f"{label_sandwich} {sandwich_total_cents}")
print(f"{label_grand} {grand_total_cents}")