a=int(input())
b=int(input())
if (a<b):
    a,b=b,a
gcd=1
for i in range(1,a):
    if a%i==0 and b%i==0:
        gcd=gcd*i
lcm=a*b//gcd
print(int(lcm),gcd)
