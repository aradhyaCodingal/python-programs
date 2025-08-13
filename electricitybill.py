unit=int(input("enter the units you consumed"))
amount=0
subcharge=0
if unit<=50:
    amount=unit*2.60
    subcharge=25
elif unit<=100:
    amount=130+((unit-50)*3.25)
    subcharge=35
elif unit<=200:
    amount=130+162.50+((unit-100)*5.26)
    subcharge=45
else:
    amount=130+162.50+526+((unit-200)*8.45)
    subcharge=75
eb=amount+subcharge
print("electricity bill=",eb)        