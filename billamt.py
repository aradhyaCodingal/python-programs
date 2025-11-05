def total_bill(billamt,tipamt):
    total=billamt*(1+0.01*tipamt)
    total=(round(total,2))
    print("total pay=",total)

total_bill(150,50)


                   
    