n=int(input())
a=bin(n)
b=list(a)
c=b[2:]
for i in c:
    print(i, end='')
