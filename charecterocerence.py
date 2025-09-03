str=input("enter a string")
ch=input("enter the letter to be checked")
i=0
count=0
lenth=len(str)
while i<lenth:
    if ( str [i] ==ch ):
        count=count+1
    i=i+1
print("the total number of times",ch,"has occered",count)

