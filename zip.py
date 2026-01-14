s1={2,3,4}
s2={'b','a','c'}
s3=list(zip(s1,s2))
print(s3)
stock=['reliance','infosys','TCS']
price=[2000,3500,4000]
new_dic={stock:price for stock,pice in zip(stock,price)}
print(new_dic)
