n=int(input())
factors=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j==n:
            factors.append(i)
prime_Factors=[]
none=[]
for factor in factors:
    if factor<2:
        none.append(factor)
    elif(factor>2 and factor==2 and factor%2!=0):
        prime_factors.append(factor)
print(prime_Factors)
