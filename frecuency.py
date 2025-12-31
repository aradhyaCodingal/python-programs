test_dictionary={'codingal':2,'is':2,'the':2,'best':2,'for':1,'coding':2}
print("og dictionary"+str(test_dictionary))
k=2
count=0
for key in test_dictionary:
    if test_dictionary[key]==k:
        count=count+1
print("frecuncy of "+str(count))
