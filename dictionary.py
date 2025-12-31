student_data={'id1':
              {'name':'abc',
               'class':'first',
               'subject':['math,comuter,science']},
              'id2':
              {'name':'pqr',
               'class':'second',
               'subject':['history,geography,coding']},
             }
result={}
for key, value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)
