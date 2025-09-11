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