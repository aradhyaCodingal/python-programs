def match_words(words):
    ctr=0
    lst=[]
    for words in (words):
        if len (words)>1 and words[0]==words[-1]:
            ctr=ctr+1
            lst.append(words)
    print("list words whose first and last charecter is the same")
    return ctr
count=match_words(['aba','cfd','xyz','uju'])
print("number of words who have the same first and last charecter=",count)