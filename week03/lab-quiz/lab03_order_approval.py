order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
is_member_input = input("Is customer a member? (yes/no): ").strip().lower()

is_member = is_member_input == "yes"

# Check for invalid quantities or insufficient stock
if requested_quantity <= 0 or requested_quantity > available_stock:
    print("Order Rejected: Invalid quantity or insufficient stock.")
else:
    # Check for member discount on orders >= 500 TRY
    if is_member and order_amount >= 500:
        final_price = order_amount * 0.90
        reason = "Approved with 10% member discount."
    else:
        final_price = order_amount
        reason = "Approved at standard price."
    
    print(f"Approval Reason: {reason}")
    print(f"Final Price: {final_price:.2f} TRY")

