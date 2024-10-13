                                                #SKIPPED PROGRAM
'''n=int(input())
b=[]
c=[]
for i in range(1,n+1):
    for j in range(i,n+1):
        if i*j==n:
            b.append(i)
        elif i!=j:
            c.append(j)
d=[]
flag=False
for k in b:
    if k==2 and k>1:
        flag=True
    elif k%2==0:
        return False
    elif k%2!=0:
        return True
if True:
    k.append(d)
print(d)

n = int(input())
factors = []  
prime_factors = []  
for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)  # Append i to factors list if it divides n
print(factors)
# Check if the factors are prime
for factor in factors:#[1, 2, 4, 5, 10, 20, 25, 50, 100]
    if factor > 1:  # Ignore 1 because it's not a prime number
        is_prime = True
        for j in range(2, int(factor**0.5) + 1):
            if factor % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_factors.append(factor)  # Append the prime factor

print(prime_factors)
'''
n=int(input())
i=1
for i in range(0,n+1):
    while i <= n:
        print(i)
    i=i+1
