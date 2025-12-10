l=[1,2,3,4,5,6]
print("og list",l)
count=0
for i in l:
    count=count+i
print("sum",count)
average=count/len(l)
print("average",average)
l.sort()
print("sorted list:",l)

print("smallest value",l[0])
print("largest value",l[-1])
      