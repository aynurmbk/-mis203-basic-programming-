
# Week 5 Lab: Reusable Shipping Quote 

def calculate_subtotal(price, quantity):
    """Calculates the subtotal for the items."""
    return price * quantity

def calculate_discount_rate(subtotal):
    """Determines the discount rate based on a threshold boundary (e.g., 100)."""
    if subtotal >= 100:
        return 0.10  # %10 discount for 100 or more
    return 0.00

def calculate_shipping_fee(subtotal):
    """Determines shipping fee based on whether subtotal meets free shipping."""
    if subtotal >= 150:
        return 0.0
    return 15.0

def calculate_final_total(price, quantity):
    """Calculates the final total using the separate functions above."""
    subtotal = calculate_subtotal(price, quantity)
    discount = subtotal * calculate_discount_rate(subtotal)
    shipping = calculate_shipping_fee(subtotal)
    final = (subtotal - discount) + shipping
    return final

# --- Acceptance Check 3: Assert Checks (including threshold boundary) ---
# Threshold boundary test for 100 subtotal
assert calculate_subtotal(50, 2) == 100
assert calculate_discount_rate(100) == 0.10
assert calculate_discount_rate(99) == 0.00
print("All assert checks passed successfully!")

# --- Call functions for at least two sample orders ---
print("\n--- Sample Order 1 ---")
order1_price = 40
order1_qty = 3  # Subtotal = 120 (qualifies for discount)
print(f"Final Total 1: {calculate_final_total(order1_price, order1_qty)}")

print("\n--- Sample Order 2 ---")
order2_price = 25
order2_qty = 2  # Subtotal = 50 (no discount, shipping fee applies)
print(f"Final Total 2: {calculate_final_total(order2_price, order2_qty)}")

# --- Acceptance Check 4: Difference between print and return ---
# 'return' sends the result back to where the function was called so it can 
# be stored in a variable and used in further calculations. 
# 'print()' simply displays the text/value on the screen to the user 
# and cannot be used in subsequent mathematical operations.

