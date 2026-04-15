import datetime

print("===== MONTHS OF THE YEAR =====")

# Loop through all months
for i in range(1, 13):
    
    # Create a date (year can be anything, day = 1)
    date_obj = datetime.date(2025, i, 1)
    
    # Get full month name
    month_name = date_obj.strftime("%B")
    
    print("Month", i, ":", month_name)

print("===== END OF PROGRAM =====")