term=int(input("Enter the term you want your fibonacci series to be of: "))
a,b=0,1
result=[]
for i in range(term):
    a,b=b,a+b
    result.append(a)
print("Your fibonacci series is: ",result)

