# Create a shopping program that asks for:
#  Customer name
#  Product price
#  Quantity
#  Membership status (yes/no)
# Calculate:
# Subtotal = price × quantity
# Apply discounts:
#  Subtotal ≥ Rs. 10,000 → 15%
#  Subtotal ≥ Rs. 5,000 → 10%
#  Subtotal ≥ Rs. 2,000 → 5%
#  Otherwise → No discount
# If the customer is a member and subtotal is at least Rs. 5,000, give an additional
# 5% discount.
# Display:
#  Customer name
#  Subtotal
#  Discount
#  Final amount
# Use f-strings.
name = input("Enter the customer's name: ")
price = float(input("Enter the product price: "))
quantity = int(input("Enter the quantity: "))
membership = input("Is the customer a member? (yes/no): ").strip().lower()
subtotal = price * quantity
if subtotal >= 10000:
    discount = 0.15
elif subtotal >= 5000:
    discount = 0.10
elif subtotal >= 2000:
    discount = 0.05
else:
    discount = 0.0
if membership== "yes" and subtotal >= 5000:
    discount += 0.05
discount_amount = subtotal * discount
final_amount = subtotal - discount_amount
print(f"Customer Name: {name}")
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Discount: Rs. {discount_amount:.2f}")
print(f"Final Amount: Rs. {final_amount:.2f}")