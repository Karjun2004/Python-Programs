a=int(input())#3
b=int(input())#6
if a<b:
    a=a
    b=b
elif(a>b):
    a=b
    b=a
gcd=1
for i in range(1,b+1):
    if a%i==0 and b%i==0:
        gcd=gcd*i
print(gcd)
