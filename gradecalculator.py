english=int(input("ënter the marks for english"))
bio=int(input("ënter the marks for bio"))
chem=int(input("ënter the marks for chem"))
history=int(input("ënter the marks for history"))
geo=int(input("ënter the marks for geo"))
total=english+bio+chem+history+geo
avarage=total/5
print("total marks are",total)
print("average marks are",avarage)
if avarage >= 90  and avarage<=100:
    print("outstanding")
elif avarage >= 80  and avarage<90:
    print("distingtion")
elif avarage >= 65 and avarage<80:
    print("first class")
elif avarage >= 50 and avarage<65:
    print("second class")
elif avarage >= 35  and avarage< 50:
    print("pass")
elif avarage < 35:
    print("fail")
else:
    print("invalid input")

 

