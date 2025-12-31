def calculate_due_amount(total_bill, amount_paid):
    due_amount = total_bill - amount_paid
    return due_amount

total = float(input("Enter total bill amount: "))
paid = float(input("Enter amount paid by customer: "))

due = calculate_due_amount(total, paid)

print("Customer due amount is:", due)