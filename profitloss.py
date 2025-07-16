actual_amount= int(input("enter the actual amount"))
sales_amount= int(input("enter the sales amount"))
if actual_amount<sales_amount:
    profit=sales_amount-actual_amount
    print("profit is:",profit)
else:
    print("you gained no profit")

