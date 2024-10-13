n=int(input())
a,b=0,1
c=[]#[0, 1, 1, 2, 3]
for i in range(n):
    c.append(a)
    a,b=b,a+b
print(c[-1]+c[-2])
