# Sales and statistics trackers
tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

# Main continuous loop
while True:
    # 1. Ask for customer name
    name = input("Customer name (or q to quit): ").strip()
    if name.lower() == 'q':
        break

    # 2. Ask for age and validate
    try:
        age = int(input("Age: "))
        if age < 0 or age > 120:
            print("Invalid age.")
            continue
    except ValueError:
        print("Invalid age.")
        continue

    # 3. Ask for day and validate
    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ["weekday", "weekend"]:
        print("Invalid day.")
        continue

    # 4. Ask for student status and validate
    student = input("Student (yes/no): ").strip().lower()
    if student not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue

    # 5. Determine base price
    if day == "weekday":
        base_price = 200.0
    else:
        base_price = 250.0

    # 6. Apply discount rules in exact specified order
    discount_category = ""
    discount_rate = 0.0

    if age < 6:
        discount_category = "Free"
        discount_rate = 1.0  # 100%
    elif age >= 65:
        discount_category = "Senior"
        discount_rate = 0.5  # 50%
    elif 6 <= age <= 12:
        discount_category = "Child"
        discount_rate = 0.4  # 40%
    elif student == "yes" and age <= 25:
        discount_category = "Student"
        discount_rate = 0.3  # 30%
    else:
        discount_category = "Standard"
        discount_rate = 0.0  # 0%

    # Calculate final price
    final_price = base_price * (1 - discount_rate)

    # Print ticket result
    print(f"{name}: {final_price:.2f} TRY ({discount_category})")

    # Update summary metrics
    tickets_sold += 1
    total_revenue += final_price
    if discount_category == "Free":
        free_tickets += 1

# Print final summary when the loop ends
if tickets_sold > 0:
    average_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold} Total revenue: {total_revenue:.2f} TRY Average price: {average_price:.2f} TRY Free tickets: {free_tickets}")
else:
    print("No tickets sold.")
