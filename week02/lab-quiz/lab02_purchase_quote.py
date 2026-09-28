#Get Inputs from user 
print("     PURCHASE QUOTE CALCULATOR     ")

Item 1 details 
item1_name = input("Enter item 1 name:")
item1_quantity= input("Enter item 1 quantity:")
item1_price= float(input("Enter item 1 unit price:"))


#Item 1 details 
item2_name = input("Enter item 2 name:")
item2_quantity= input("Enter item 2 quantity:")
item2_price= float(input("Enter item 2 unit price:"))

# Delivery and Tax Details 
delivery_fee = float(input("Enter delivery fee:"))
tax_percentage = float(input("Enter tax percentage (%) :"))


# 2.Calculations 
line1_total = item1_quantity * item1_price
line2_ total = item2_quantity * item2_price

subtotal = line1_total + line2_total 
tax_amountt = subtotal *(tax_percentage / 100)
total = subtotal + tax_amount + delivery_free

# 3. Print outputs 
print ( "\n")
print ("PURCHASE QUOTE SUMMARY")
print(f"{item1_name}:{item1_quantity} * {item1_price:.2f} TRY = {line1_total:.2f} TRY")
print(f"{item2_name}: {item2_quantity } * {item2_price:.2f} TRY = {line2_total:.2f} TRY")
print("f"Subtotal: {subtotal:.2f} TRY")
print(f"" Tax ({tax_percentage:.0f}%): {tax_amount:.2f } TRY")
print (f" delivery fee: {delivery_fee:.2f} TRY")
print (f"TOTAL:.2f} TRY")

* Acceptance Check #4 Explanation
print ("\n[EXPLANATION]: input() returns data as a string by default.")
print "(Performing arithmetic on strings either causes a TypeError or unexpected concatenation (e.g.,12' + '2' = '22').")
print ("Therefore, inputs must be converted to int or float before performing mathematical calculations.")
