# Lab 03 - Order Approval Policy

This folder contains the order approval policy program (`lab03_order_approval.py`) and testing notes.

## Boundary Test Cases (500 TRY Threshold)

The table below shows the testing results for values around the 500 TRY member discount boundary:

| Test Case | Order Amount | Is Member? | Requested / Stock | Expected & Actual Result |
| :--- | :--- | :--- | :--- | :--- |
| Below Boundary | 499 TRY | Yes | 1 / 10 | Approved at standard price (499.00 TRY) |
| Exactly Boundary | 500 TRY | Yes | 1 / 10 | Approved with 10% discount (450.00 TRY) |
| Above Boundary | 501 TRY | Yes | 1 / 10 | Approved with 10% discount (450.90 TRY) |

## Testing Notes & Modifications

- **Test Executed:** Ran the code with an input of 500 TRY for a member to ensure the boundary condition inclusion (`>= 500`).
- **Modification Made:** Updated the member check condition to handle user input case-insensitively using `.strip().lower()` so that inputs like `" Yes "` or `"YES"` are recognized correctly.
